from task_1_2_0_hidden_message import pattern_count
from task_1_2_1_frequent_words import better_frequent_words, frequent_words


def test_pattern_count() -> None:
    count = pattern_count("AGGTCATCAGG", "AGG")
    assert count == 2


def test_frequent_words() -> None:
    freq_patterns = frequent_words("CTTAGAGTGCTTGGAGACTTATAGA", 3)
    assert freq_patterns == {"AGA", "CTT"}


def test_better_frequent_words() -> None:
    freq_patterns = better_frequent_words("CTTAGAGTGCTTGGAGACTTATAGA", 3)
    assert freq_patterns == {"AGA", "CTT"}
