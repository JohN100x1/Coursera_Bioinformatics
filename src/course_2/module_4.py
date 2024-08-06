from collections import Counter
from typing import Iterable

from course_2.module_3 import AMINO_ACID_MASS, cyclic_spectrum, linear_spectrum


def get_spectrum_score(expected: list[int], spectrum: list[int]) -> int:
    """Returns the score for the expected spectrum compared to actual."""
    actual_masses = Counter(spectrum)
    return sum(
        min(freq, actual_masses[mass])
        for mass, freq in Counter(expected).items()
        if mass in actual_masses
    )


def cyclic_peptide_score(
    peptide: str | tuple[int, ...], spectrum: list[int]
) -> int:
    """Returns the score for a peptide against a spectrum."""
    theoretical_spectrum = cyclic_spectrum(peptide)
    return get_spectrum_score(theoretical_spectrum, spectrum)


def linear_peptide_score(
    peptide: str | tuple[int, ...], spectrum: list[int]
) -> int:
    """Returns the score for a peptide against a spectrum."""
    theoretical_spectrum = linear_spectrum(peptide)
    return get_spectrum_score(theoretical_spectrum, spectrum)


def trim[
    T: str | tuple[int, ...]
](leaderboard: Iterable[T], spectrum: list[int], n: int) -> set[T]:
    """
    Returns peptides with the top n linear peptide scores including ties,
    given as mass tuples.
    """
    if not leaderboard:
        return set()
    scores = sorted(
        [
            (peptide, linear_peptide_score(peptide, spectrum))
            for peptide in leaderboard
        ],
        key=lambda x: x[1],
        reverse=True,
    )

    cutoff_score = scores[min(n, len(scores)) - 1][1]
    return {peptide for peptide, score in scores if score >= cutoff_score}


def leaderboard_cyclic_peptide_sequencing(
    spectrum: list[int], n: int, masses: Iterable[int] | None = None
) -> set[str]:
    """
    Returns leader peptide for spectrum based on highest linear peptide score.
    """
    if masses is None:
        masses = set(AMINO_ACID_MASS.values())

    def expand(peptides: set[tuple[int, ...]]) -> set[tuple[int, ...]]:
        return {p + (mass,) for p in peptides for mass in masses}

    leaderboard: set[tuple[int, ...]] = {tuple()}
    leaders = set()
    leader_score = -1
    while leaderboard:
        leaderboard = expand(leaderboard)
        remaining = set()
        for peptide in leaderboard:
            if sum(peptide) == spectrum[-1]:
                score = cyclic_peptide_score(peptide, spectrum)
                if score > leader_score:
                    leaders = {peptide}
                    leader_score = score
                elif score == leader_score:
                    leaders.add(peptide)
                remaining.add(peptide)
            elif sum(peptide) < spectrum[-1]:
                remaining.add(peptide)
        leaderboard = trim(remaining, spectrum, n)
    return {"-".join(str(x) for x in leader) for leader in leaders}


def convolution(spectrum: list[int]) -> list[int]:
    """Returns the convolution of a spectrum."""
    spectrum.sort()
    return [
        spectrum[i] - spectrum[j]
        for i in range(len(spectrum))
        for j in range(i)
        if spectrum[i] - spectrum[j] > 0
    ]


def convolution_cyclic_peptide_sequencing(
    spectrum: list[int], m: int, n: int
) -> set[str]:
    """Returns leader peptide for spectrum based on spectrum convolution."""
    mass_counts = Counter([m for m in convolution(spectrum) if 57 <= m <= 200])
    mass_freq = sorted(mass_counts.items(), key=lambda x: x[1], reverse=True)

    cutoff_freq = mass_freq[min(m, len(mass_freq)) - 1][1]
    masses = [mass for mass, freq in mass_freq if freq >= cutoff_freq]
    return leaderboard_cyclic_peptide_sequencing(spectrum, n, masses)
