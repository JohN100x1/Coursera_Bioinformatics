from task_1_2_1_frequent_words import frequency_table


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
