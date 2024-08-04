import pytest

from course_3.module_2 import (
    edit_distance,
    fitting_alignment,
    global_alignment,
    local_alignment,
    overlap_alignment,
)


@pytest.mark.parametrize(
    "v, w, reward, mismatch, in_del, expected",
    [
        # ("GAGA", "GAT", 1, 1, 2, (-1, "GAGA", "GA-T")), # TODO: fix
        ("ACG", "ACT", 1, 3, 1, (0, "AC-G", "ACT-")),
        ("AT", "AG", 1, 1, 1, (0, "AT", "AG")),
        ("TCA", "CA", 2, 5, 1, (3, "TCA", "-CA")),
        ("TTTTCCTT", "CC", 1, 10, 1, (-4, "TTTTCCTT", "----CC--")),
        ("ACAGATTAG", "T", 2, 3, 2, (-14, "ACAGATTAG", "-----T---")),
        ("G", "ACATACGATG", 3, 1, 2, (-15, "------G---", "ACATACGATG")),
    ],
)
def test_global_alignment(
    v: str,
    w: str,
    reward: int,
    mismatch: int,
    in_del: int,
    expected: tuple[int, str, str],
) -> None:
    assert global_alignment(v, w, reward, mismatch, in_del) == expected


@pytest.mark.parametrize(
    "v, w, reward, mismatch, in_del, expected",
    [
        ("MEANLY", "PENALTY", None, None, 5, (15, "EANL-Y", "ENALTY")),
        ("GAGA", "GAT", 1, 1, 2, (2, "GA", "GA")),
        ("AGC", "ATC", 3, 3, 1, (4, "A-GC", "AT-C")),
        ("AT", "AG", 1, 1, 1, (1, "A", "A")),
        ("TAACG", "ACG", 1, 1, 1, (3, "ACG", "ACG")),
        ("CAGAGATGGCCG", "ACG", 3, 2, 1, (6, "CG", "CG")),
        ("CTT", "AGCATAAAGCATT", 2, 3, 1, (5, "C-TT", "CATT")),
    ],
)
def test_local_alignment(
    v: str,
    w: str,
    reward: int,
    mismatch: int,
    in_del: int,
    expected: tuple[int, str, str],
) -> None:
    assert local_alignment(v, w, reward, mismatch, in_del) == expected


@pytest.mark.parametrize(
    "v, w, distance",
    [
        ("GAGA", "GAT", 2),
        ("AC", "AC", 0),
        ("AT", "G", 2),
        ("CAGACCGAGTTAG", "CGG", 10),
        ("CGT", "CAGACGGTGACG", 9),
    ],
)
def test_edit_distance(v: str, w: str, distance: int) -> None:
    assert edit_distance(v, w) == distance


@pytest.mark.parametrize(
    "v, w, expected",
    [
        ("DISCREPANTLY", "PATENT", (20, "PA--NT", "PATENT")),
        ("ARKANSAS", "SASS", (11, "SAS-", "SASS")),
        ("DISCREPANTLY", "DISCRETE", (34, "DISCREPANT-", "DISCRE---TE")),
        ("CANT", "CA", (13, "CA", "CA")),
    ],
)
def test_fitting_alignment(
    v: str, w: str, expected: tuple[int, str, str]
) -> None:
    assert fitting_alignment(v, w) == expected


@pytest.mark.parametrize(
    "v, w, reward, mismatch, in_del, expected",
    [
        ("GAGA", "GAT", 1, 1, 2, (2, "GA", "GA")),
        ("CCAT", "AT", 1, 1, 1, (2, "AT", "AT")),
        ("GAT", "CAT", 1, 5, 1, (1, "-AT", "CAT")),
        ("ATCACT", "AT", 1, 5, 1, (1, "ACT", "A-T")),
        ("ATCACT", "ATG", 1, 1, 5, (0, "CT", "AT")),
        ("CAGAGATGGCCG", "ACG", 3, 2, 1, (5, "-CG", "ACG")),
        ("CTT", "AGCATAAAGCATT", 2, 3, 1, (0, "--CT-T", "AGC-AT")),
    ],
)
def test_overlap_alignment(
    v: str,
    w: str,
    reward: int,
    mismatch: int,
    in_del: int,
    expected: tuple[int, str, str],
) -> None:
    assert overlap_alignment(v, w, reward, mismatch, in_del) == expected
