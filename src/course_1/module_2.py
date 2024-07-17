from collections import defaultdict

from course_1.module_1 import reverse_complement

NUCLEOTIDES = {"A", "C", "G", "T"}


def find_min_skew(text: str) -> list[int]:
    """Find and return the indexes where skew is the minimum."""
    skew = 0
    min_idx = []
    min_skew = 0
    for i, base in enumerate(text, 1):
        if base == "G":
            skew += 1
        elif base == "C":
            skew -= 1
        if skew == min_skew:
            min_idx.append(i)
        elif skew < min_skew:
            min_idx = [i]
            min_skew = skew
    return min_idx


def hamming_distance(kmer1: str, kmer2: str) -> int:
    """Returns the hamming distance between two k-mers."""
    if len(kmer1) != len(kmer2):
        raise ValueError("kmer1 and kmer2 must be the same length.")
    return sum(1 for n1, n2 in zip(kmer1, kmer2) if n1 != n2)


def approximate_match(pattern: str, text: str, d: int) -> list[int]:
    """Returns a list of patterns in text with hamming distance <= d."""
    indexes = []
    k = len(pattern)
    for i in range(len(text) - k + 1):
        if hamming_distance(pattern, text[i : i + k]) <= d:
            indexes.append(i)
    return indexes


def approximate_count(pattern: str, text: str, d: int) -> int:
    """Returns a count of patterns in text with hamming distance <= d."""
    count = 0
    k = len(pattern)
    for i in range(len(text) - k + 1):
        if hamming_distance(pattern, text[i : i + k]) <= d:
            count += 1
    return count


def neighbours(pattern: str, d: int) -> set[str]:
    """
    Returns a set of patterns in the neighbourhood of pattern.
    i.e. patterns same as pattern with hamming distance <= d.
    """
    if d == 0:
        return {pattern}
    if len(pattern) == 1:
        return NUCLEOTIDES
    neighbourhood = set()
    suffix_pattern = pattern[1:]
    for text in neighbours(suffix_pattern, d):
        if hamming_distance(suffix_pattern, text) < d:
            for nucleotide in NUCLEOTIDES:
                neighbourhood.add(nucleotide + text)
        else:
            neighbourhood.add(pattern[0] + text)
    return neighbourhood


def frequent_words_with_mismatch(text: str, k: int, d: int) -> set[str]:
    """
    Returns a set of the most frequent k-length patterns (k-mers) in text with
    mismatches.
    """
    freq_map = defaultdict(int)
    for i in range(len(text) - k + 1):
        for neighbour in neighbours(text[i : i + k], d):
            freq_map[neighbour] += 1
    freq_max = max(freq_map.values())
    return {pattern for pattern, freq in freq_map.items() if freq == freq_max}


def frequent_words_with_mismatch_rc(text: str, k: int, d: int) -> set[str]:
    """
    Returns a set of the most frequent k-length patterns (k-mers) in text with
    mismatches and reverse compliments.
    """
    freq_map = defaultdict(int)
    for i in range(len(text) - k + 1):
        for neighbour in neighbours(text[i : i + k], d):
            freq_map[neighbour] += 1
    text_rc = reverse_complement(text)
    for i in range(len(text) - k + 1):
        for neighbour in neighbours(text_rc[i : i + k], d):
            freq_map[neighbour] += 1
    freq_max = max(freq_map.values())
    return {pattern for pattern, freq in freq_map.items() if freq == freq_max}
