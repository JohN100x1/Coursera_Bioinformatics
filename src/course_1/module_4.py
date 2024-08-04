from math import inf, prod
from random import choices, randint

from course_1.module_3 import motif_profile, motif_score, profile_probable_kmer


def profile_probable_motifs(
    dna: list[str], profile: list[list[float]]
) -> list[str]:
    """Returns the profile-most probable motifs from dna."""
    k = len(profile[0])
    return [profile_probable_kmer(text, k, profile) for text in dna]


def randomised_motif_search(dna: list[str], k: int, t: int) -> list[str]:
    """Return the best motifs from a random starting motifs."""
    motifs = []
    for string in dna[:t]:
        start_index = randint(0, len(string) - k)
        motifs.append(string[start_index : start_index + k])
    best_motifs = motifs
    best_score = motif_score(motifs)
    while True:
        profile = motif_profile(motifs, laplace=True)
        motifs = profile_probable_motifs(dna, profile)
        score = motif_score(motifs)
        if score < best_score:
            best_motifs = motifs
            best_score = score
        else:
            return best_motifs


def repeated_random_motif_search(
    dna: list[str], k: int, t: int, repeats: int
) -> list[str]:
    """Return the best motifs by score using repeating random motif search."""
    best_motifs = []
    best_score = inf
    for _ in range(repeats):
        motifs = randomised_motif_search(dna, k, t)
        score = motif_score(motifs)
        if score < best_score:
            best_motifs = motifs
            best_score = score
    return best_motifs


def gibbs_sampler(dna: list[str], k: int, t: int, n: int) -> list[str]:
    """Return the best motifs using Gibbs sampling."""
    idx_map = {"A": 0, "C": 1, "G": 2, "T": 3}
    motifs = []
    for string in dna[:t]:
        start_index = randint(0, len(string) - k)
        motifs.append(string[start_index : start_index + k])
    best_motifs = motifs
    best_score = motif_score(motifs)
    for _ in range(n):
        i = randint(0, t - 1)
        profile = motif_profile(motifs[:i] + motifs[i + 1 :], laplace=True)
        kmers = [dna[i][idx : idx + k] for idx in range(len(dna[0]) - k + 1)]
        weights = [
            prod(profile[idx_map[char]][j] for j, char in enumerate(kmer))
            for kmer in kmers
        ]
        motif = choices(kmers, weights=weights)[0]
        motifs = motifs[:i] + [motif] + motifs[i + 1 :]
        score = motif_score(motifs)
        if score < best_score:
            best_motifs = motifs
            best_score = score
    return best_motifs


def repeated_gibbs_sampler(
    dna: list[str], k: int, t: int, n: int, repeats: int
) -> list[str]:
    """Return the best motifs using repeated Gibbs sampling."""
    best_motifs = []
    best_score = inf
    for _ in range(repeats):
        motifs = gibbs_sampler(dna, k, t, n)
        score = motif_score(motifs)
        if score < best_score:
            best_motifs = motifs
            best_score = score
    return best_motifs
