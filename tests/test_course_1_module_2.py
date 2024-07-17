from course_1.module_2 import (
    approximate_count,
    approximate_match,
    find_min_skew,
    frequent_words_with_mismatch,
    frequent_words_with_mismatch_rc,
    hamming_distance,
    neighbours,
)


def test_pattern_count() -> None:
    mins = find_min_skew("TAAAGACTGCCGAGAGGCCAACACGAGTGCTAGAACGAGGGGCGTAAA")
    assert mins == [11, 24]


def test_hamming_distance() -> None:
    dist = hamming_distance("GGGCCGTTGGT", "GGACCGTTGAC")
    assert dist == 3


def test_approximate_match() -> None:
    matches = approximate_match("CAC", "ACACACACA", 1)
    assert matches == [1, 3, 5]


def test_approximate_count() -> None:
    count = approximate_count("GAGG", "TTTAGAGCCTTCAGAGG", 2)
    assert count == 4


def test_neighbours() -> None:
    neighbourhood = neighbours("AC", 1)
    assert neighbourhood == {"AG", "AA", "AT", "TC", "GC", "CC", "AC"}


def test_frequent_words_with_mismatch() -> None:
    kmers = frequent_words_with_mismatch("ACGTTGCATGTCGCATGATGCATGAGAGC", 4, 1)
    assert kmers == {"GATG", "ATGC", "ATGT"}


def test_frequent_words_with_mismatch_rc() -> None:
    kmers = frequent_words_with_mismatch_rc(
        "ACGTTGCATGTCGCATGATGCATGAGAGCT", 4, 1
    )
    assert kmers == {"ATGT", "ACAT"}
