from course_2.module_4 import (
    convolution,
    convolution_cyclic_peptide_sequencing,
    cyclic_peptide_score,
    leaderboard_cyclic_peptide_sequencing,
    linear_peptide_score,
    trim,
)


def test_cyclic_peptide_score() -> None:
    spectrum = [0, 99, 113, 114, 128, 227, 257, 299, 355, 356, 370, 371, 484]
    assert cyclic_peptide_score("NQEL", spectrum) == 11


def test_linear_peptide_score() -> None:
    spectrum = [0, 99, 113, 114, 128, 227, 257, 299, 355, 356, 370, 371, 484]
    assert linear_peptide_score("NQEL", spectrum) == 8


def test_trim() -> None:
    spectrum = trim(
        ["LAST", "ALST", "TLLT", "TQAS"],
        [0, 71, 87, 101, 113, 158, 184, 188, 259, 271, 372],
        2,
    )
    assert spectrum == {"LAST", "ALST"}


def test_leaderboard_cyclic_peptide_sequencing() -> None:
    spectrum = [0, 71, 113, 129, 147, 200, 218, 260, 313, 331, 347, 389, 460]
    peptides = leaderboard_cyclic_peptide_sequencing(spectrum, 10)
    assert "113-129-71-147" in peptides


def test_convolution() -> None:
    assert convolution([0, 137, 186, 323]) == [137, 186, 49, 323, 186, 137]


def test_convolution_cyclic_peptide_sequencing() -> None:
    peptides = convolution_cyclic_peptide_sequencing(
        [
            57,
            57,
            71,
            99,
            129,
            137,
            170,
            186,
            194,
            208,
            228,
            265,
            285,
            299,
            307,
            323,
            356,
            364,
            394,
            422,
            493,
        ],
        20,
        60,
    )
    assert "57-137-71-99-57-72" in peptides
