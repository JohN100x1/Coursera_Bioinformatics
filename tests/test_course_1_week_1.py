from course_1.week_1 import (
    better_frequent_words,
    find_clumps,
    frequent_words,
    pattern_count,
    pattern_matching,
    reverse_complement,
)


def test_pattern_count() -> None:
    count = pattern_count("AGGTCATCAGG", "AGG")
    assert count == 2


def test_frequent_words() -> None:
    freq_patterns = frequent_words("CTTAGAGTGCTTGGAGACTTATAGA", 3)
    assert freq_patterns == {"AGA", "CTT"}


def test_better_frequent_words() -> None:
    freq_patterns = better_frequent_words("CTTAGAGTGCTTGGAGACTTATAGA", 3)
    assert freq_patterns == {"AGA", "CTT"}


def test_reverse_complement() -> None:
    complement = reverse_complement("AAAACCCGGT")
    assert complement == "ACCGGGTTTT"


def test_pattern_matching() -> None:
    indexes = pattern_matching("ATAT", "GATATATGCATATACTT")
    assert indexes == [1, 3, 9]


def test_find_clumps() -> None:
    text = (
        "CGGACTCGACAGATGTGAAGAACGACAATGTGAAGAC"
        "TCGACACGACAGAGTGAAGAGAAGAGGAAACATTGTAA"
    )
    patterns = find_clumps(text, 5, 50, 4)
    assert patterns == {"CGACA", "GAAGA"}
