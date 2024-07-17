from random import seed

from course_2.module_2 import (
    eulerian_cycle,
    eulerian_path,
    generate_contigs,
    k_universal_circular_string,
    maximal_non_branching_paths,
    paired_string_reconstruction,
    string_reconstruction,
    string_spelled_by_gapped_patterns,
)


def test_eulerian_cycle() -> None:
    seed(0)
    cycle = eulerian_cycle(
        {
            0: [3],
            1: [0],
            2: [1, 6],
            3: [2],
            4: [2],
            5: [4],
            6: [5, 8],
            7: [9],
            8: [7],
            9: [6],
        }
    )
    assert cycle == [6, 5, 4, 2, 1, 0, 3, 2, 6, 8, 7, 9, 6]


def test_eulerian_path() -> None:
    seed(0)
    path = eulerian_path(
        {0: [2], 1: [3], 2: [1], 3: [0, 4], 6: [3, 7], 7: [8], 8: [9], 9: [6]}
    )
    assert path == [6, 7, 8, 9, 6, 3, 0, 2, 1, 3, 4]


def test_string_reconstruction() -> None:
    seed(0)
    text = string_reconstruction(
        ["CTTA", "ACCA", "TACC", "GGCT", "GCTT", "TTAC"]
    )
    assert text == "GGCTTACCA"


def test_k_universal_string() -> None:
    seed(0)
    string = k_universal_circular_string(3)
    assert string == "11000101"


def test_string_spelled_by_gapped_patterns() -> None:
    string = string_spelled_by_gapped_patterns(
        [
            ("GACC", "GCGC"),
            ("ACCG", "CGCC"),
            ("CCGA", "GCCG"),
            ("CGAG", "CCGG"),
            ("GAGC", "CGGA"),
        ],
        4,
        2,
    )
    assert string == "GACCGAGCGCCGGA"


def test_paired_string_reconstruction() -> None:
    string = paired_string_reconstruction(
        [
            ("GAGA", "TTGA"),
            ("TCGT", "GATG"),
            ("CGTG", "ATGT"),
            ("TGGT", "TGAG"),
            ("GTGA", "TGTT"),
            ("GTGG", "GTGA"),
            ("TGAG", "GTTG"),
            ("GGTC", "GAGA"),
            ("GTCG", "AGAT"),
        ],
        4,
        2,
    )
    assert string == "GTGGTCGTGAGATGTTGA"


def test_maximal_non_branching_paths() -> None:
    paths = maximal_non_branching_paths(
        {1: [2], 2: [3], 3: [4, 5], 6: [7], 7: [6]}
    )
    assert paths == [[1, 2, 3], [3, 4], [3, 5], [6, 7, 6]]


def test_generate_contigs() -> None:
    contigs = generate_contigs(
        ["ATG", "ATG", "TGT", "TGG", "CAT", "GGA", "GAT", "AGA"]
    )
    assert sorted(contigs) == sorted(
        ["AGA", "ATG", "ATG", "CAT", "GAT", "TGGA", "TGT"]
    )
