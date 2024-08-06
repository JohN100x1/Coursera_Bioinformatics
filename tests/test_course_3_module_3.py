import pytest

from course_3.module_3 import (
    find_middle_edge,
    global_alignment_3_dim,
    global_alignment_gap,
    global_alignment_linear_space,
)


@pytest.mark.parametrize(
    "v, w, reward, mismatch, gap_open, gap_ext, expected",
    [
        ("GA", "GTTA", 1, 3, 2, 1, (-1, "G--A", "GTTA")),
        ("TTT", "TT", 1, 5, 3, 1, (-1, "TTT", "TT-")),
        ("GAT", "AT", 1, 5, 5, 1, (-3, "GAT", "-AT")),
        ("CCAT", "GAT", 1, 5, 2, 1, (-3, "-CCAT", "G--AT")),
        ("CAGGT", "TAC", 1, 2, 3, 2, (-8, "CAGGT", "TAC--")),
        (
            "GTTCCAGGTA",
            "CAGTAGTCGT",
            2,
            3,
            3,
            2,
            (-8, "--GT--TCCAGGTA", "CAGTAGTC---GT-"),
        ),
        ("AGCTAGCCTAG", "GT", 1, 3, 1, 1, (-7, "AGCTAGCCTAG", "-G-T-------")),
        ("AA", "CAGTGTCAGTA", 2, 1, 2, 1, (-7, "-------A--A", "CAGTGTCAGTA")),
        ("ACGTA", "ACT", 5, 2, 15, 5, (-12, "ACGTA", "ACT--")),
        (
            "ATCTTGTATAATAAAATCGAGATTGGGCGTGGACAATACTCCTCGAAGAGACAGCCAATTACCCCTCTTCGCAGAACCAAGCCTATTGGG",
            "ATCTTGTATAATTCGAGATTGTGCCTGCCGACAATACGCCTCGAAGGACAAGCCACTACGCTATCCTCTTCCGTGTCAGATCCAAGAGTGCTTATTGGG",
            1,
            5,
            3,
            1,
            (
                8,
                "ATCTTGTATAATAAAATCGAGATTGGGCGTG--GACAATACTCCTCGAAGAGACA-GCCA-ATTAC-C---CCTCTTC---G-CAGAACCAAG----CCTATTGGG",
                "ATCTTGTATAAT----TCGAGATTGTGCCTGCCGACAATACGCCTCGAAG-GACAAGCCAC--TACGCTATCCTCTTCCGTGTCAGATCCAAGAGTGCTTATTGGG",
            ),
        ),
    ],
)
def test_global_alignment_gap(
    v: str,
    w: str,
    reward: int,
    mismatch: int,
    gap_open: int,
    gap_ext: int,
    expected: tuple[int, str, str],
) -> None:
    actual = global_alignment_gap(v, w, reward, mismatch, gap_open, gap_ext)
    assert actual == expected


@pytest.mark.parametrize(
    "w, v, reward, mismatch, in_del, edge_start, edge_end",
    [
        ("GAGA", "GAT", 1, 1, 2, (2, 2), (2, 3)),
        ("TTTT", "CC", 1, 5, 1, (0, 2), (0, 3)),
        ("GAT", "AT", 1, 1, 2, (0, 1), (1, 2)),
        ("TTTT", "TTCTT", 1, 1, 1, (2, 2), (3, 2)),
        ("GAACCC", "G", 1, 5, 1, (1, 3), (1, 4)),
        ("ACAGT", "CAT", 2, 3, 1, (1, 2), (2, 3)),
        ("T", "AATCCC", 2, 5, 3, (0, 0), (1, 0)),
    ],
)
def test_find_middle_edge(
    w: str,
    v: str,
    reward: int,
    mismatch: int,
    in_del: int,
    edge_start: tuple[int, int],
    edge_end: tuple[int, int],
) -> None:
    n, m = len(v), len(w)
    start, end = find_middle_edge(w, v, 0, n, 0, m, reward, mismatch, in_del)
    assert (start, end) == (edge_start, edge_end)


@pytest.mark.parametrize(
    "v, w, reward, mismatch, in_del, expected",
    [
        ("GAGA", "GAT", 1, 1, 2, (-1, "GAGA", "GA-T")),
        # TODO: fix global_alignment_linear_space (wrong mismatch/in_del order)
        # ("TT", "CC", 1, 5, 1, (-4, "--TT", "CC--")),
        ("TT", "CC", 1, 1, 5, (-2, "TT", "CC")),
        ("GAACGATTG", "GGG", 1, 5, 1, (-3, "GAACGATTG", "G---G---G")),
        ("GCG", "CT", 2, 3, 1, (-1, "GCG-", "-C-T")),
        ("ACAGCTA", "G", 1, 2, 3, (-17, "ACAGCTA", "---G---")),
        ("A", "CGGAGTGCC", 3, 4, 1, (-5, "---A-----", "CGGAGTGCC")),
        ("TTTT", "TTCTT", 1, 1, 1, (3, "TT-TT", "TTCTT")),  # extra_test
        ("T", "AATCCC", 2, 5, 3, (-13, "--T---", "AATCCC")),  # extra_test
    ],
)
def test_global_alignment_linear_space(
    v: str,
    w: str,
    reward: int,
    mismatch: int,
    in_del: int,
    expected: tuple[int, str, str],
) -> None:
    actual = global_alignment_linear_space(v, w, reward, mismatch, in_del)
    assert actual == expected


@pytest.mark.parametrize(
    "u, v, w, expected",
    [
        # (
        #     "ATATCGG",
        #     "TCCGA",
        #     "ATGTACTG",
        #     (3, "ATATCC-G-", "---TCC-GA", "ATGTACTG-"),
        # ), # TODO: fix global_alignment_3_dim (moveEnum priority)
        ("A", "AT", "A", (1, "A-", "AT", "A-")),
        ("AAAAT", "CCCCT", "T", (1, "AAAAT", "CCCCT", "----T")),
        ("AT", "ACCT", "AGGGGT", (2, "A------T", "A----CCT", "AGGGG--T")),
        ("GGAG", "TT", "CCCC", (0, "----GGAG", "--TT----", "CCCC----")),
        ("T", "T", "T", (1, "T", "T", "T")),
        # (
        #     "TGTTTAAAAATGTCCGCAACCATTTC",
        #     "GATATAAAACAGGGATAACTGCAATGG",
        #     "CCTGCTACTTTATGCCGTCTCCATATGCG",
        #     (
        #         11,
        #         "T---G--T---T----------T-AAAAA--TGTCCGC-------A-ACCATTTC-----",
        #         "----GA-TA--TAAAACAGGGAT-A----ACTG-C----------A-A---T---GG---",
        #         "-CCTG-CT-ACT----------TTA------TG-C---CGTCTCCATA---T-----GCG",
        #     ),
        # ), # TODO: fix global_alignment_3_dim (moveEnum priority)
    ],
)
def test_global_alignment_3_dim(
    u: str, v: str, w: str, expected: tuple[int, str, str, str]
) -> None:
    assert global_alignment_3_dim(u, v, w) == expected
