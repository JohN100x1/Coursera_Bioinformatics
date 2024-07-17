from collections import defaultdict


def pattern_count(text: str, pattern: str) -> int:
    """Count the number of occurrences of pattern in text."""
    k = len(pattern)
    return sum(
        1 for i in range(len(text) - k + 1) if text[i : i + k] == pattern
    )


def frequent_words(text: str, k: int) -> set[str]:
    """
    Returns a set of the most frequent k-length patterns (k-mers) in text.
    """
    freq_patterns = set()
    counts = [0 for _ in range(len(text) - k + 1)]
    for i in range(len(text) - k + 1):
        counts[i] = pattern_count(text, text[i : i + k])
    max_count = max(counts)
    for i in range(len(text) - k + 1):
        if counts[i] == max_count:
            freq_patterns.add(text[i : i + k])
    return freq_patterns


def frequency_table(text: str, k: int) -> dict[str, int]:
    """Returns a frequency map of k-length patterns (k-mers) in text."""
    freq_map: dict[str, int] = defaultdict(int)
    for i in range(len(text) - k + 1):
        freq_map[text[i : i + k]] += 1
    return freq_map


def better_frequent_words(text: str, k: int) -> set[str]:
    """
    Returns a set of the most frequent k-length patterns (k-mers) in text.
    (faster)
    """
    freq_map = frequency_table(text, k)
    freq_max = max(freq_map.values())
    return {pattern for pattern, freq in freq_map.items() if freq == freq_max}


def reverse_complement(pattern: str) -> str:
    """Returns the reverse complement of a DNA pattern."""
    translation_table = str.maketrans("ACGT", "TGCA")
    translated_string = pattern.translate(translation_table)
    return translated_string[::-1]


def pattern_matching(pattern: str, genome: str) -> list[int]:
    """Returns a list of starting indexes for pattern in genome."""
    k = len(pattern)
    return [
        i for i in range(len(genome) - k + 1) if genome[i : i + k] == pattern
    ]


def find_clumps(text: str, k: int, length: int, t: int) -> set[str]:
    """Returns a set of k-mer patterns forming (L, t)-clumps in text."""
    freq_map = frequency_table(text[:length], k)
    patterns = {pattern for pattern, freq in freq_map.items() if freq >= t}
    for i in range(1, len(text) - length + 1):
        kmer_start = text[i - 1 : i + k - 1]
        kmer_end = text[i + length - k : i + length]
        freq_map[kmer_start] -= 1
        freq_map[kmer_end] += 1
        if freq_map[kmer_end] >= t:
            patterns.add(kmer_end)
    return patterns
