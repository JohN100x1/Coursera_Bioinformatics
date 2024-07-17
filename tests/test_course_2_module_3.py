from course_2.module_3 import (
    translate_rna,
    peptide_encodes,
    cyclic_sub_peptide_count,
    linear_spectrum,
    cyclic_spectrum,
    count_peptides,
    linear_sub_peptide_count,
    cyclo_peptide_sequencing,
)


def test_translate_rna() -> None:
    string = translate_rna(
        "AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA"
    )
    assert string == "MAMAPRTEINSTRING"


def test_peptide_encode() -> None:
    substrings = peptide_encodes(
        "ATGGCCATGGCCCCCAGAACTGAGATCAATAGTACCCGTATTAACGGGTGA", "MA"
    )
    assert sorted(substrings) == ["ATGGCC", "ATGGCC", "GGCCAT"]


def test_cyclic_sub_peptide_count() -> None:
    assert cyclic_sub_peptide_count(31315) == 980597910


def test_linear_sub_peptide_count() -> None:
    assert linear_sub_peptide_count(29354) == 430843336


def test_linear_spectrum() -> None:
    spectrum = linear_spectrum("NQEL")
    assert spectrum == [0, 113, 114, 128, 129, 242, 242, 257, 370, 371, 484]


def test_cyclic_spectrum() -> None:
    spectrum = cyclic_spectrum("NQEL")
    assert spectrum == [
        0,
        113,
        114,
        128,
        129,
        227,
        242,
        242,
        257,
        355,
        356,
        370,
        371,
        484,
    ]


def test_count_peptides() -> None:
    assert count_peptides(1024) == 14712706211


def test_cyclo_peptide_sequencing() -> None:
    assert cyclo_peptide_sequencing(
        [0, 113, 128, 186, 241, 299, 314, 427]
    ) == [
        "113-128-186",
        "113-186-128",
        "186-113-128",
        "128-186-113",
        "186-128-113",
        "128-113-186",
    ]
