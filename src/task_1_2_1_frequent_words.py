from collections import defaultdict

from task_1_2_0_hidden_message import pattern_count


def frequent_words(text: str, k: int) -> set[str]:
    """Returns a set of the most frequent k-length patterns (k-mers) in text."""
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
    """Returns a set of the most frequent k-length patterns (k-mers) in text. (faster)"""
    freq_map = frequency_table(text, k)
    freq_max = max(freq_map.values())
    return {pattern for pattern, freq in freq_map.items() if freq == freq_max}
