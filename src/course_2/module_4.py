from collections import Counter
from typing import Iterable

from course_2.module_3 import (
    AMINO_ACID_MASS,
    cyclic_spectrum,
    cyclo_spectrum,
    lin_spectrum,
    linear_spectrum,
)


def get_spectrum_score(expected: list[int], spectrum: list[int]) -> int:
    """Returns the score for the expected spectrum compared to actual."""
    actual_masses = Counter(spectrum)
    return sum(
        min(freq, actual_masses[mass])
        for mass, freq in Counter(expected).items()
        if mass in actual_masses
    )


def cyclic_peptide_score(peptide: str, spectrum: list[int]) -> int:
    """Returns the score for a peptide against a spectrum."""
    theoretical_spectrum = cyclic_spectrum(peptide)
    return get_spectrum_score(theoretical_spectrum, spectrum)


def linear_peptide_score(peptide: str, spectrum: list[int]) -> int:
    """Returns the score for a peptide against a spectrum."""
    theoretical_spectrum = linear_spectrum(peptide)
    return get_spectrum_score(theoretical_spectrum, spectrum)


def trim(leaderboard: list[str], spectrum: list[int], n: int) -> list[str]:
    """Returns peptides with the top n linear peptide scores including ties."""
    if not leaderboard:
        return []
    scores = sorted(
        [
            (peptide, linear_peptide_score(peptide, spectrum))
            for peptide in leaderboard
        ],
        key=lambda x: x[1],
        reverse=True,
    )

    cutoff_score = scores[min(n, len(scores)) - 1][1]
    return [peptide for peptide, score in scores if score >= cutoff_score]


def cyclo_peptide_score(peptide: tuple[int, ...], spectrum: list[int]) -> int:
    """
    Returns score for cyclic peptide against a spectrum, given as a mass tuple.
    """
    theoretical_spectrum = cyclo_spectrum(peptide)
    return get_spectrum_score(theoretical_spectrum, spectrum)


def lin_peptide_score(peptide: tuple[int, ...], spectrum: list[int]) -> int:
    """
    Returns score for linear peptide against a spectrum, given as a mass tuple.
    """
    theoretical_spectrum = lin_spectrum(peptide)
    return get_spectrum_score(theoretical_spectrum, spectrum)


def trim_tuple(
    leaderboard: Iterable[tuple[int, ...]], spectrum: list[int], n: int
) -> list[tuple[int, ...]]:
    """
    Returns peptides with the top n linear peptide scores including ties,
    given as mass tuples.
    """
    if not leaderboard:
        return []
    scores = sorted(
        [
            (peptide, lin_peptide_score(peptide, spectrum))
            for peptide in leaderboard
        ],
        key=lambda x: x[1],
        reverse=True,
    )

    cutoff_score = scores[min(n, len(scores)) - 1][1]
    return [peptide for peptide, score in scores if score >= cutoff_score]


def leaderboard_cyclo_peptide_sequencing(
    spectrum: list[int], n: int, masses: Iterable[int] | None = None
) -> set[str]:
    """
    Returns leader peptide for spectrum based on highest linear peptide score.
    """
    if masses is None:
        masses = set(AMINO_ACID_MASS.values())

    def expand(peptides: set[tuple[int, ...]]) -> set[tuple[int, ...]]:
        return {p + (mass,) for p in peptides for mass in masses}

    leaderboard = {()}
    leaders = set()
    leader_score = -1
    while leaderboard:
        leaderboard = expand(leaderboard)
        remaining = set()
        for peptide in leaderboard:
            if sum(peptide) == spectrum[-1]:
                score = cyclo_peptide_score(peptide, spectrum)
                if score > leader_score:
                    leaders = {peptide}
                    leader_score = score
                elif score == leader_score:
                    leaders.add(peptide)
                remaining.add(peptide)
            elif sum(peptide) < spectrum[-1]:
                remaining.add(peptide)
        leaderboard = trim_tuple(remaining, spectrum, n)
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


def convolution_cyclo_peptide_sequencing(
    spectrum: list[int], m: int, n: int
) -> set[str]:
    """Returns leader peptide for spectrum based on spectrum convolution."""
    mass_counts = Counter([m for m in convolution(spectrum) if 57 <= m <= 200])
    mass_freq = sorted(mass_counts.items(), key=lambda x: x[1], reverse=True)

    cutoff_freq = mass_freq[min(m, len(mass_freq)) - 1][1]
    masses = [mass for mass, freq in mass_freq if freq >= cutoff_freq]
    return leaderboard_cyclo_peptide_sequencing(spectrum, n, masses)
