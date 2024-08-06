import pytest

from course_1.module_2 import (
    approximate_count,
    approximate_match,
    find_min_skew,
    frequent_words_with_mismatch,
    frequent_words_with_mismatch_rc,
    hamming_distance,
    neighbours,
)


@pytest.mark.parametrize(
    "text, indexes",
    [
        (
            "TAAAGACTGCCGAGAGGCCAACACGAGTGCTAGAACGAGGGGCGTAAACGCGGGTCCGAT",
            [11, 24],
        ),
        ("ACCG", [3]),
        ("ACCC", [4]),
        ("CCGGGT", [2]),
        ("CCGGCCGG", [2, 6]),
    ],
)
def test_pattern_count(text: str, indexes: list[int]) -> None:
    assert find_min_skew(text) == indexes


@pytest.mark.parametrize(
    "kmer1, kmer2, dist",
    [
        ("GGGCCGTTGGT", "GGACCGTTGAC", 3),
        ("AAAA", "TTTT", 4),
        ("ACGTACGT", "TACGTACG", 8),
        ("ACGTACGT", "CCCCCCCC", 6),
        ("ACGTACGT", "TGCATGCA", 8),
        (
            "GATAGCAGCTTCTGAACTGGTTACCTGCCGTGAGTAAATTAAAATTTTATTGACTTAGGTCACTA"
            "AATACT",
            "AATAGCAGCTTCTCAACTGGTTACCTCGTATGAGTAAATTAGGTCATTATTGACTCAGGTCACTA"
            "ACGTCT",
            15,
        ),
        (
            "AGAAACAGACCGCTATGTTCAACGATTTGTTTTATCTCGTCACCGGGATATTGCGGCCACTCATC"
            "GGTCAGTTGATTACGCAGGGCGTAAATCGCCAGAATCAGGCTG",
            "AGAAACCCACCGCTAAAAACAACGATTTGCGTAGTCAGGTCACCGGGATATTGCGGCCACTAAGG"
            "CCTTGGATGATTACGCAGAACGTATTGACCCAGAATCAGGCTC",
            28,
        ),
    ],
)
def test_hamming_distance(kmer1: str, kmer2: str, dist: int) -> None:
    assert hamming_distance(kmer1, kmer2) == dist


@pytest.mark.parametrize(
    "pattern, text, d, indexes",
    [
        (
            "ATTCTGGA",
            "CGCCCGAATCCAGAACGCATTCCCATATTTCGGGACCACTGGCCTCCACGGTACGGACGTCAATC"
            "AAAT",
            3,
            [6, 7, 26, 27],
        ),
        (
            "AAA",
            "TTTTTTAAATTTTAAATTTTTT",
            2,
            [4, 5, 6, 7, 8, 11, 12, 13, 14, 15],
        ),
        (
            "GAGCGCTGG",
            "GAGCGCTGGGTTAACTCGCTACTTCCCGACGAGCGCTGTGGCGCAAATTGGCGATGAAACTGCAG"
            "AGAGAACTGGTCATCCAACTGAATTCTCCCCGCTATCGCATTTTGATGCGCGCCGCGTCGATT",
            2,
            [0, 30, 66],
        ),
        (
            "AATCCTTTCA",
            "CCAAATCCCCTCATGGCATGCATTCCCGCAGTATTTAATCCTTTCATTCTGCATATAAGTAGTGA"
            "AGGTATAGAAACCCGTTCAAGCCCGCAGCGGTAAAACCGAGAACCATGATGAATGCACGGCGATT"
            "GCGCCATAATCCAAACA",
            3,
            [3, 36, 74, 137],
        ),
        (
            "CCGTCATCC",
            "CCGTCATCCGTCATCCTCGCCACGTTGGCATGCATTCCGTCATCCCGTCAGGCATACTTCTGCAT"
            "ATAAGTACAAACATCCGTCATGTCAAAGGGAGCCCGCAGCGGTAAAACCGAGAACCATGATGAAT"
            "GCACGGCGATTGC",
            3,
            [0, 7, 36, 44, 48, 72, 79, 112],
        ),
        ("TTT", "AAAAAA", 3, [0, 1, 2, 3]),
        ("CCA", "CCACCT", 0, [0]),
    ],
)
def test_approximate_match(
    pattern: str, text: str, d: int, indexes: list[int]
) -> None:
    assert approximate_match(pattern, text, d) == indexes


@pytest.mark.parametrize(
    "pattern, text, d, count",
    [
        ("GAGG", "TTTAGAGCCTTCAGAGG", 2, 4),
        (
            "TACAG",
            "GAATCCGCCAAGTACCAAGATGTAAGTGAGGAGCGCTTAGGTCTGTACTGCGCATAAGCCTTAAC"
            "GCGAAGTATGGATATGCTCCCCGGATACAGGTTTGGGATTTGGCGGTTACCTAAGCTAACGGTGA"
            "GACCGATATGACGAGGTTCCTATCTTAATCATATTCACATACTGAACGAGGCGCCCAGTTTCTTC"
            "TCACCAATATGTCAGGAAGCTACAGTGCAGCATTATCCACACCATTCCACTTATCCTTGAACGGA"
            "AGTCTTATGCGAAGATTATTCTGAGAAGCCCTTGTGCCCTGCATCACGATTTGCAGACTGACAGG"
            "GAATCTTAAGGCCACTCAAA",
            2,
            27,
        ),
    ],
)
def test_approximate_count(
    pattern: str, text: str, d: int, count: int
) -> None:
    assert approximate_count(pattern, text, d) == count


@pytest.mark.parametrize(
    "pattern, d, neighbourhood",
    [
        (
            "ACG",
            1,
            {
                "ATG",
                "ACT",
                "TCG",
                "AAG",
                "CCG",
                "ACA",
                "ACC",
                "ACG",
                "GCG",
                "AGG",
            },
        ),
        ("AGA", 0, {"AGA"}),
        (
            "AAA",
            1,
            {
                "TAA",
                "CAA",
                "AGA",
                "AAG",
                "AAA",
                "GAA",
                "AAC",
                "ACA",
                "AAT",
                "ATA",
            },
        ),
        ("A", 1, {"A", "C", "G", "T"}),
    ],
)
def test_neighbours(pattern: str, d: int, neighbourhood: set[str]) -> None:
    neighbourhood = neighbours("AC", 1)
    assert neighbourhood == {"AG", "AA", "AT", "TC", "GC", "CC", "AC"}


@pytest.mark.parametrize(
    "text, k, d, kmers",
    [
        ("ACGTTGCATGTCGCATGATGCATGAGAGCT", 4, 1, {"ATGC", "ATGT", "GATG"}),
        ("AGGT", 2, 1, {"GG"}),
        ("AGGGT", 2, 0, {"GG"}),
        ("AGGCGG", 3, 0, {"AGG", "GGC", "GCG", "CGG"}),
    ],
)
def test_frequent_words_with_mismatch(
    text: str, k: int, d: int, kmers: set[str]
) -> None:
    assert frequent_words_with_mismatch(text, k, d) == kmers


@pytest.mark.parametrize(
    "text, k, d, kmers",
    [
        ("ACGTTGCATGTCGCATGATGCATGAGAGCT", 4, 1, {"ACAT", "ATGT"}),
        ("AAAAAAAAAA", 2, 1, {"AT", "TA"}),
        ("AGTCAGTC", 4, 2, {"AATT", "GGCC"}),
        ("AATTAATTGGTAGGTAGGTA", 4, 0, {"AATT"}),
        (
            "ATA",
            3,
            1,
            {
                "ATG",
                "AGA",
                "GAT",
                "TTA",
                "AAA",
                "CAT",
                "AAT",
                "TCT",
                "CTA",
                "ATA",
                "TAG",
                "TAC",
                "ACA",
                "GTA",
                "ATC",
                "TAA",
                "ATT",
                "TAT",
                "TTT",
                "TGT",
            },
        ),
        ("AAT", 3, 0, {"AAT", "ATT"}),
        ("TAGCG", 2, 1, {"CC", "TG", "CA", "GG"}),
    ],
)
def test_frequent_words_with_mismatch_rc(
    text: str, k: int, d: int, kmers: set[str]
) -> None:
    assert frequent_words_with_mismatch_rc(text, k, d) == kmers
