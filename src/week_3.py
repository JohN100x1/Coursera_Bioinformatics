from itertools import product
from math import inf, log2, prod

from week_2 import frequent_words_with_mismatch, hamming_distance


def motif_enumeration(dna: list[str], k: int, d: int) -> set[str]:
    """Returns a set of k-mers in dna with hamming distance <= d."""
    patterns = set()
    texts = [{txt[i : i + k] for i in range(len(txt) - k + 1)} for txt in dna]
    for kmer1 in set.union(*texts):
        for kmer2 in frequent_words_with_mismatch(kmer1, k, d):
            for kmers in texts:
                for pattern in kmers:
                    if hamming_distance(kmer2, pattern) <= d:
                        break  # Match found, look at next text
                else:
                    break  # No match for kmer2 in text, stop looking
            else:
                patterns.add(kmer2)
    return patterns


def motif_profile(dna: list[str]) -> list[list[float]]:
    """Returns the profile matrix of dna."""
    profile = [[] for _ in range(4)]
    idx_map = {"A": 0, "C": 1, "G": 2, "T": 3}
    for i in range(len(dna[0])):
        counts = [0, 0, 0, 0]
        for text in dna:
            counts[idx_map[text[i]]] += 1
        for j, c in enumerate(counts):
            profile[j].append(c / len(dna))
    return profile


def motif_laplace_profile(dna: list[str]) -> list[list[float]]:
    """Returns the profile matrix of dna with laplace rule applied."""
    profile = [[] for _ in range(4)]
    idx_map = {"A": 0, "C": 1, "G": 2, "T": 3}
    for i in range(len(dna[0])):
        counts = [1, 1, 1, 1]
        for text in dna:
            counts[idx_map[text[i]]] += 1
        for j, c in enumerate(counts):
            profile[j].append(c / (len(dna) + 4))
    return profile


def motif_score(motifs: list[str]) -> int:
    """Returns the score of a motif matrix."""
    idx_map = {"A": 0, "C": 1, "G": 2, "T": 3}
    score = len(motifs) * len(motifs[0])
    for i in range(len(motifs[0])):
        counts = [0, 0, 0, 0]
        for motif in motifs:
            counts[idx_map[motif[i]]] += 1
        score -= max(counts)
    return score


def motif_entropy(dna: list[str]) -> float:
    """Returns the entropy of the matrix of dna."""
    profile = motif_profile(dna)
    return -sum(p * log2(p) for col in profile for p in col if p > 0)


def dna_hamming_distance(pattern: str, dna: list[str]) -> int:
    """Returns the hamming distance of pattern in dna."""
    k = len(pattern)
    return sum(
        min(
            hamming_distance(pattern, txt[i : i + k])
            for i in range(len(txt) - k + 1)
        )
        for txt in dna
    )


def median_strings(dna: list[str], k: int) -> list[str]:
    """Returns the median patterns in the dna."""
    dist = inf
    medians = []
    for kmer_tuple in product("ACGT", repeat=k):
        kmer = "".join(kmer_tuple)
        kmer_dist = dna_hamming_distance(kmer, dna)
        if kmer_dist < dist:
            dist = kmer_dist
            medians = [kmer]
        elif kmer_dist == dist:
            medians.append(kmer)
    return medians


def profile_probable_kmer(
    text: str, k: int, profile: list[list[float]]
) -> str:
    """Returns the profile-most probable kmer from text."""
    idx_map = {"A": 0, "C": 1, "G": 2, "T": 3}
    max_prob = 0
    max_pattern = ""
    for i in range(len(text) - k + 1):
        pattern = text[i : i + k]
        prob = prod(
            profile[idx_map[nucleotide]][j]
            for j, nucleotide in enumerate(pattern)
        )
        if prob > max_prob:
            max_prob = prob
            max_pattern = pattern
    return max_pattern


def greedy_motif_search(dna: list[str], k: int, t: int) -> list[str]:
    """Return the best motifs using greedy search."""
    best_motifs = [text[:k] for text in dna]
    best_score = motif_score(best_motifs)
    for i in range(len(dna[0]) - k + 1):
        motifs = [dna[0][i : i + k]]
        for j in range(1, t):
            profile = motif_profile(motifs)
            motif = profile_probable_kmer(dna[j], k, profile) or dna[j][:k]
            motifs.append(motif)
        score = motif_score(motifs)
        if score < best_score:
            best_motifs = motifs
            best_score = score
    return best_motifs


def improved_greedy_motif_search(dna: list[str], k: int, t: int) -> list[str]:
    """Return the best motifs using greedy search with pseudo-counts."""
    best_motifs = [text[:k] for text in dna]
    best_score = motif_score(best_motifs)
    for i in range(len(dna[0]) - k + 1):
        motifs = [dna[0][i : i + k]]
        for j in range(1, t):
            profile = motif_laplace_profile(motifs)
            motif = profile_probable_kmer(dna[j], k, profile) or dna[j][:k]
            motifs.append(motif)
        score = motif_score(motifs)
        if score < best_score:
            best_motifs = motifs
            best_score = score
    return best_motifs
