import pytest

from course_1.module_1 import (
    better_frequent_words,
    find_clumps,
    frequent_words,
    pattern_count,
    pattern_matching,
    reverse_complement,
)


@pytest.mark.parametrize(
    "text, pattern, count",
    [
        ("GCGCG", "GCG", 2),
        ("ACGTACGTACGT", "CG", 3),
        (
            "AAAGAGTGTCTGATAGCAGCTTCTGAACTGGTTACCTGCCGTGAGTAAATTAAATTTTATTGACT"
            "TAGGTCACTAAATACTTTAACCAATATAGGCATAGCGCACAGACAGATAATAATTACAGAGTACA"
            "CAACATCCAT",
            "AAA",
            4,
        ),
        (
            "AGCGTGCCGAAATATGCCGCCAGACCTGCTGCGGTGGCCTCGCCGACTTCACGGATGCCAAGTGC"
            "ATAGAGGAAGCGAGCAAAGGTGGTTTCTTTCGCTTTATCCAGCGCGTTAACCACGTTCTGTGCCG"
            "ACTTT",
            "TTT",
            4,
        ),
        ("GGACTTACTGACGTACG", "ACT", 2),
        ("ATCCGATCCCATGCCCATG", "CC", 5),
        (
            "CTGTTTTTGATCCATGATATGTTATCTCTCCGTCATCAGAAGAACAGTGACGGATCGCCCTCTCT"
            "CTTGGTCAGGCGACCGTTTGCCATAATGCCCATGCTTTCCAGCCAGCTCTCAAACTCCGGTGACT"
            "CGCGCAGGTTGAGTA",
            "CTC",
            9,
        ),
    ],
)
def test_pattern_count(text: str, pattern: str, count: int) -> None:
    assert pattern_count(text, pattern) == count


@pytest.mark.parametrize(
    "text, k, patterns",
    [
        ("ACGTTGCATGTCGCATGATGCATGAGAGCT", 4, {"CATG", "GCAT"}),
        (
            "TGGTAGCGACGTTGGTCCCGCCGCTTGAGAATCTGGATGAACATAAGCTCCCACTTGGCTTATTC"
            "AGAGAACTGGTCAACACTTGTCTCTCCCAGCCAGGTCTGACCACCGGGCAACTTTTAGAGCACTA"
            "TCGTGGTACAAATAATGCTGCCAC",
            3,
            {"TGG"},
        ),
        (
            "CAGTGGCAGATGACATTTTGCTGGTCGACTGGTTACAACAACGCCTGGGGCTTTTGAGCAACGAG"
            "ACTTTTCAATGTTGCACCGTTTGCTGCATGATATTGAAAACAATATCACCAAATAAATAACGCCT"
            "TAGTAAGTAGCTTTT",
            4,
            {"TTTT"},
        ),
        (
            "ATACAATTACAGTCTGGAACCGGATGAACTGGCCGCAGGTTAACAACAGAGTTGCCAGGCACTGC"
            "CGCTGACCAGCAACAACAACAATGACTTTGACGCGAAGGGGATGGCATGAGCGAACTGATCGTCA"
            "GCCGTCAGCAACGAGTATTGTTGCTGACCCTTAACAATCCCGCCGCACGTAATGCGCTAACTAAT"
            "GCCCTGCTG",
            5,
            {"AACAA"},
        ),
        (
            "CCAGCGGGGGTTGATGCTCTGGGGGTCACAAGATTGCATTTTTATGGGGTTGCAAAAATGTTTTT"
            "TACGGCAGATTCATTTAAAATGCCCACTGGCTGGAGACATAGCCCGGATGCGCGTCTTTTACAAC"
            "GTATTGCGGGGTAAAATCGTAGATGTTTTAAAATAGGCGTAAC",
            5,
            {"AAAAT", "GGGGT", "TTTTA"},
        ),
        (
            "CGGAAGCGAGATTCGCGTGGCGTGATTCCGGCGGGCGTGGAGAAGCGAGATTCATTCAAGCCGGG"
            "AGGCGTGGCGTGGCGTGGCGTGCGGATTCAAGCCGGCGGGCGTGATTCGAGCGGCGGATTCGAGA"
            "TTCCGGGCGTGCGGGCGTGAAGCGCGTGGAGGAGGCGTGGCGTGCGGGAGGAGAAGCGAGAAGCC"
            "GGATTCAAGCAAGCATTCCGGCGGGAGATTCGCGTGGAGGCGTGGAGGCGTGGAGGCGTGCGGCG"
            "GGAGATTCAAGCCGGATTCGCGTGGAGAAGCGAGAAGCGCGTGCGGAAGCGAGGAGGAGAAGCAT"
            "TCGCGTGATTCCGGGAGATTCAAGCATTCGCGTGCGGCGGGAGATTCAAGCGAGGAGGCGTGAAG"
            "CAAGCAAGCAAGCGCGTGGCGTGCGGCGGGAGAAGCAAGCGCGTGATTCGAGCGGGCGTGCGGAA"
            "GCGAGCGG",
            12,
            {
                "CGTGGCGTGCGG",
                "TGCGGCGGGAGA",
                "GTGCGGCGGGAG",
                "CGGGAGATTCAA",
                "GGAGATTCAAGC",
                "GCGTGGAGGCGT",
                "GGAGAAGCGAGA",
                "CGTGCGGCGGGA",
                "GCGTGGCGTGCG",
                "CGTGGAGGCGTG",
                "GGCGGGAGATTC",
                "GGGAGATTCAAG",
                "GCGTGCGGCGGG",
                "CGGCGGGAGATT",
            },
        ),
    ],
)
def test_frequent_words(text: str, k: int, patterns: set[str]) -> None:
    assert frequent_words(text, k) == patterns


@pytest.mark.parametrize(
    "text, k, patterns",
    [
        ("ACGTTGCATGTCGCATGATGCATGAGAGCT", 4, {"CATG", "GCAT"}),
        (
            "TGGTAGCGACGTTGGTCCCGCCGCTTGAGAATCTGGATGAACATAAGCTCCCACTTGGCTTATTC"
            "AGAGAACTGGTCAACACTTGTCTCTCCCAGCCAGGTCTGACCACCGGGCAACTTTTAGAGCACTA"
            "TCGTGGTACAAATAATGCTGCCAC",
            3,
            {"TGG"},
        ),
        (
            "CAGTGGCAGATGACATTTTGCTGGTCGACTGGTTACAACAACGCCTGGGGCTTTTGAGCAACGAG"
            "ACTTTTCAATGTTGCACCGTTTGCTGCATGATATTGAAAACAATATCACCAAATAAATAACGCCT"
            "TAGTAAGTAGCTTTT",
            4,
            {"TTTT"},
        ),
        (
            "ATACAATTACAGTCTGGAACCGGATGAACTGGCCGCAGGTTAACAACAGAGTTGCCAGGCACTGC"
            "CGCTGACCAGCAACAACAACAATGACTTTGACGCGAAGGGGATGGCATGAGCGAACTGATCGTCA"
            "GCCGTCAGCAACGAGTATTGTTGCTGACCCTTAACAATCCCGCCGCACGTAATGCGCTAACTAAT"
            "GCCCTGCTG",
            5,
            {"AACAA"},
        ),
        (
            "CCAGCGGGGGTTGATGCTCTGGGGGTCACAAGATTGCATTTTTATGGGGTTGCAAAAATGTTTTT"
            "TACGGCAGATTCATTTAAAATGCCCACTGGCTGGAGACATAGCCCGGATGCGCGTCTTTTACAAC"
            "GTATTGCGGGGTAAAATCGTAGATGTTTTAAAATAGGCGTAAC",
            5,
            {"AAAAT", "GGGGT", "TTTTA"},
        ),
        (
            "CGGAAGCGAGATTCGCGTGGCGTGATTCCGGCGGGCGTGGAGAAGCGAGATTCATTCAAGCCGGG"
            "AGGCGTGGCGTGGCGTGGCGTGCGGATTCAAGCCGGCGGGCGTGATTCGAGCGGCGGATTCGAGA"
            "TTCCGGGCGTGCGGGCGTGAAGCGCGTGGAGGAGGCGTGGCGTGCGGGAGGAGAAGCGAGAAGCC"
            "GGATTCAAGCAAGCATTCCGGCGGGAGATTCGCGTGGAGGCGTGGAGGCGTGGAGGCGTGCGGCG"
            "GGAGATTCAAGCCGGATTCGCGTGGAGAAGCGAGAAGCGCGTGCGGAAGCGAGGAGGAGAAGCAT"
            "TCGCGTGATTCCGGGAGATTCAAGCATTCGCGTGCGGCGGGAGATTCAAGCGAGGAGGCGTGAAG"
            "CAAGCAAGCAAGCGCGTGGCGTGCGGCGGGAGAAGCAAGCGCGTGATTCGAGCGGGCGTGCGGAA"
            "GCGAGCGG",
            12,
            {
                "CGTGGCGTGCGG",
                "TGCGGCGGGAGA",
                "GTGCGGCGGGAG",
                "CGGGAGATTCAA",
                "GGAGATTCAAGC",
                "GCGTGGAGGCGT",
                "GGAGAAGCGAGA",
                "CGTGCGGCGGGA",
                "GCGTGGCGTGCG",
                "CGTGGAGGCGTG",
                "GGCGGGAGATTC",
                "GGGAGATTCAAG",
                "GCGTGCGGCGGG",
                "CGGCGGGAGATT",
            },
        ),
    ],
)
def test_better_frequent_words(text: str, k: int, patterns: set[str]) -> None:
    assert better_frequent_words(text, k) == patterns


@pytest.mark.parametrize(
    "pattern, complement", [("AAAACCCGGT", "ACCGGGTTTT"), ("ACACAC", "GTGTGT")]
)
def test_reverse_complement(pattern: str, complement: str) -> None:
    assert reverse_complement(pattern) == complement


@pytest.mark.parametrize(
    "pattern, genome, indexes",
    [
        ("ATAT", "GATATATGCATATACTT", [1, 3, 9]),
        ("ACAC", "TTTTACACTTTTTTGTGTAAAAA", [4]),
        (
            "AAA",
            "AAAGAGTGTCTGATAGCAGCTTCTGAACTGGTTACCTGCCGTGAGTAAATTAAATTTTATTGACT"
            "TAGGTCACTAAATACTTTAACCAATATAGGCATAGCGCACAGACAGATAATAATTACAGAGTACA"
            "CAACATCCAT",
            [0, 46, 51, 74],
        ),
        (
            "TTT",
            "AGCGTGCCGAAATATGCCGCCAGACCTGCTGCGGTGGCCTCGCCGACTTCACGGATGCCAAGTGC"
            "ATAGAGGAAGCGAGCAAAGGTGGTTTCTTTCGCTTTATCCAGCGCGTTAACCACGTTCTGTGCCG"
            "ACTTT",
            [88, 92, 98, 132],
        ),
        ("ATA", "ATATATA", [0, 2, 4]),
    ],
)
def test_pattern_matching(
    pattern: str, genome: str, indexes: list[int]
) -> None:
    assert pattern_matching(pattern, genome) == indexes


@pytest.mark.parametrize(
    "text, k, length, t, patterns",
    [
        (
            "CGGACTCGACAGATGTGAAGAAATGTGAAGACTGAGTGAAGAGAAGAGGAAACACGACACGACAT"
            "TGCGACATAATGTACGAATGTAATGTGCCTATGGC",
            5,
            75,
            4,
            {"CGACA", "GAAGA", "AATGT"},
        ),
        ("AAAACGTCGAAAAA", 2, 4, 2, {"AA"}),
        ("ACGTACGT", 1, 5, 2, {"A", "C", "G", "T"}),
        (
            "CCACGCGGTGTACGCTGCAAAAAGCCTTGCTGAATCAAATAAGGTTCCAGCACATCCTCAATGGT"
            "TTCACGTTCTTCGCCAATGGCTGCCGCCAGGTTATCCAGACCTACAGGTCCACCAAAGAACTTAT"
            "CGATTACCGCCAGCAACAATTTGCGGTCCATATAATCGAAACCTTCAGCATCGACATTCAACATA"
            "TCCAGCG",
            3,
            25,
            3,
            {"AAA", "CCA", "CAG", "CAT", "GCC", "TTC"},
        ),
    ],
)
def test_find_clumps(
    text: str, k: int, length: int, t: int, patterns: set[str]
) -> None:
    assert find_clumps(text, k, length, t) == patterns
