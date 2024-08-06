from random import seed

import pytest

from course_2.module_2 import (
    eulerian_cycle,
    eulerian_path,
    generate_contigs,
    k_universal_circular_string,
    maximal_non_branching_paths,
    pair,
    paired_string_reconstruction,
    string_reconstruction,
    string_spelled_by_gapped_patterns,
)


@pytest.mark.parametrize(
    "graph, cycle",
    [
        (
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
            },
            [6, 5, 4, 2, 1, 0, 3, 2, 6, 8, 7, 9, 6],
        ),
        ({0: [1], 1: [2], 2: [0]}, [0, 1, 2, 0]),
        ({0: [3, 1], 1: [2], 2: [0], 3: [0]}, [0, 3, 0, 1, 2, 0]),
        ({0: [1], 1: [2, 3], 2: [0], 3: [4], 4: [1]}, [4, 1, 2, 0, 1, 3, 4]),
        ({1: [2], 2: [1, 2]}, [2, 2, 1, 2]),
        (
            {1: [10], 10: [2, 3, 4], 2: [1], 3: [10], 4: [5], 5: [10]},
            [1, 10, 4, 5, 10, 3, 10, 2, 1],
        ),
        (
            {
                0: [1, 2, 3, 4],
                1: [0, 2, 3, 4],
                2: [0, 1, 3, 4],
                3: [0, 1, 2, 4],
                4: [0, 1, 2, 3],
            },
            [3, 4, 3, 1, 3, 0, 2, 0, 4, 0, 3, 2, 1, 0, 1, 2, 4, 1, 4, 2, 3],
        ),
    ],
)
def test_eulerian_cycle(graph: dict[int, list[int]], cycle: list[int]) -> None:
    result = eulerian_cycle(graph, start=cycle[0])
    edges = {(result[i], result[i + 1]) for i in range(len(result) - 1)}
    cycle_edges = {(cycle[i], cycle[i + 1]) for i in range(len(cycle) - 1)}
    assert edges == cycle_edges


@pytest.mark.parametrize(
    "graph, path",
    [
        (
            {
                0: [2],
                1: [3],
                2: [1],
                3: [0, 4],
                6: [3, 7],
                7: [8],
                8: [9],
                9: [6],
            },
            [6, 7, 8, 9, 6, 3, 0, 2, 1, 3, 4],
        ),
        ({0: [1], 1: [2], 2: [3]}, [0, 1, 2, 3]),
        ({0: [1], 1: [2, 5], 2: [3], 3: [4], 4: [1]}, [0, 1, 2, 3, 4, 1, 5]),
        (
            {2: [1], 1: [3, 4, 0], 3: [1, 4], 4: [3, 1]},
            [2, 1, 3, 1, 4, 3, 4, 1, 0],
        ),
        (
            {
                0: [1],
                1: [14, 17],
                14: [2, 3, 4],
                2: [1],
                3: [14],
                4: [5],
                5: [14],
            },
            [0, 1, 14, 3, 14, 4, 5, 14, 2, 1, 17],
        ),
        (
            {2: [3, 5], 3: [4], 4: [2], 5: [6], 6: [2], 1: [2, 0], 0: [1]},
            [1, 0, 1, 2, 3, 4, 2, 5, 6, 2],
        ),
    ],
)
def test_eulerian_path(graph: dict[int, list[int]], path: list[int]) -> None:
    result = eulerian_path(graph)
    edges = {(result[i], result[i + 1]) for i in range(len(result) - 1)}
    path_edges = {(path[i], path[i + 1]) for i in range(len(path) - 1)}
    assert edges == path_edges


@pytest.mark.parametrize(
    "kmers, text",
    [
        (["CTTA", "ACCA", "TACC", "GGCT", "GCTT", "TTAC"], "GGCTTACCA"),
        (["ACG", "CGT", "GTG", "TGT", "GTA", "TAT", "ATA"], "ACGTGTATA"),
        (["GG", "AC", "GA", "CT"], "GGACT"),
        (["AAC", "AAC", "ACG", "ACT", "CGA", "GAA"], "AACGAACT"),
        (
            ["CTAC", "CTCC", "TCCT", "ACTC", "CCTC", "CCTA", "TACT"],
            "CCTACTCCTC",
        ),
        (
            ["CCC", "CCC", "CCC", "TCC", "CCC", "CCG", "CCC", "CCC", "CCC"],
            "TCCCCCCCCCG",
        ),
        (
            ["AG", "AT", "AA", "GA", "GG", "GT", "TA", "TG", "TT", "AT"],
            "AAGTTGGATAT",
        ),
        (["ACG", "CGT", "GTA", "TAC"], "ACGTAC"),
    ],
)
def test_string_reconstruction(kmers: list[str], text: str) -> None:
    k = len(kmers[0])
    result = string_reconstruction(kmers)
    assert len(result) == len(text)
    actual = sorted(result[i : i + k] for i in range(len(result) - k + 1))
    expected = sorted(text[i : i + k] for i in range(len(text) - k + 1))
    assert actual == expected


@pytest.mark.parametrize(
    "k, string", [(3, "00111010"), (4, "1010111100100001")]
)
def test_k_universal_string(k: int, string: str) -> None:
    result = k_universal_circular_string(k)
    assert len(result) == len(string)
    result = result + result[: k - 1]
    string = string + string[: k - 1]
    actual = sorted(result[i : i + k] for i in range(len(result) - k + 1))
    expected = sorted(string[i : i + k] for i in range(len(string) - k + 1))
    assert actual == expected


@pytest.mark.parametrize(
    "kmer_pairs, k, d, string",
    [
        (
            [
                ("GACC", "GCGC"),
                ("ACCG", "CGCC"),
                ("CCGA", "GCCG"),
                ("CGAG", "CCGG"),
                ("GAGC", "CGGA"),
            ],
            4,
            2,
            "GACCGAGCGCCGGA",
        ),
        (
            [
                ("GACA", "TCTC"),
                ("ACAC", "CTCT"),
                ("CACA", "TCTC"),
                ("ACAT", "CTCA"),
            ],
            4,
            2,
            "GACACATCTCTCA",
        ),
        (
            [("AC", "TT"), ("CG", "TG"), ("GT", "GA"), ("TT", "AC")],
            2,
            1,
            "ACGTTGAC",
        ),
        (
            [
                ("GC", "CG"),
                ("CA", "GT"),
                ("AT", "TG"),
                ("TA", "GC"),
                ("AC", "CA"),
                ("CC", "AT"),
            ],
            2,
            4,
            "GCATACCGTGCAT",
        ),
        (
            [
                ("ACAGC", "GCGAA"),
                ("CAGCT", "CGAAT"),
                ("AGCTG", "GAATC"),
                ("GCTGC", "AATCA"),
            ],
            5,
            1,
            "ACAGCTGCGAATCA",
        ),
    ],
)
def test_string_spelled_by_gapped_patterns(
    kmer_pairs: list[pair], k: int, d: int, string: str
) -> None:
    assert string_spelled_by_gapped_patterns(kmer_pairs, k, d) == string


@pytest.mark.parametrize(
    "kmer_pairs, k, d, string",
    [
        (
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
            "GTGGTCGTGAGATGTTGA",
        ),
        (
            [
                ("ACAC", "CTCT"),
                ("ACAT", "CTCA"),
                ("CACA", "TCTC"),
                ("GACA", "TCTC"),
            ],
            4,
            2,
            "GACACATCTCTCA",
        ),
        (
            [("TCA", "GCA"), ("TTC", "TGC"), ("AAT", "CAT"), ("ATT", "ATG")],
            3,
            1,
            "AATTCATGCA",
        ),
        # (
        #     [
        #         ("GG", "GA"),
        #         ("GT", "AT"),
        #         ("TG", "TA"),
        #         ("GA", "AC"),
        #         ("AT", "CT"),
        #     ],
        #     2,
        #     1,
        #     "GGTGATACT",
        # ),  # TODO: fix paired_string_reconstruction (idk what's wrong)
        # TODO: fix paired_string_reconstruction (deal with cycles)
        # (
        #     [
        #         ("GTTT", "ATTT"),
        #         ("TTTA", "TTTG"),
        #         ("TTAC", "TTGT"),
        #         ("TACG", "TGTA"),
        #         ("ACGT", "GTAT"),
        #         ("CGTT", "TATT"),
        #     ],
        #     4,
        #     2,
        #     "TTTACGTTTGTATTT",
        # ),
        (
            [
                ("GGG", "GGG"),
                ("AGG", "GGG"),
                ("GGG", "GGT"),
                ("GGG", "GGG"),
                ("GGG", "GGG"),
            ],
            3,
            2,
            "AGGGGGGGGGGT",
        ),
    ],
)
def test_paired_string_reconstruction(
    kmer_pairs: list[pair], k: int, d: int, string: str
) -> None:
    result = paired_string_reconstruction(kmer_pairs, k, d)
    assert len(result) == len(string)
    actual = [
        (result[i : i + k], result[i + k + d : i + 2 * k + d])
        for i in range(len(result) - 2 * k - d + 1)
    ]
    expected = [
        (string[i : i + k], string[i + k + d : i + 2 * k + d])
        for i in range(len(string) - 2 * k - d + 1)
    ]
    assert sorted(actual) == sorted(expected)


@pytest.mark.parametrize(
    "graph, paths",
    [
        (
            {1: [2], 2: [3], 3: [4, 5], 6: [7], 7: [6]},
            [[1, 2, 3], [3, 4], [3, 5], [6, 7, 6]],
        ),
        ({0: [1], 1: [2], 2: [3, 4]}, [[0, 1, 2], [2, 3], [2, 4]]),
        ({1: [2], 2: [6], 3: [4], 5: [3], 6: [1]}, [[5, 3, 4], [6, 1, 2, 6]]),
        (
            {1: [2], 2: [3, 4, 5], 4: [6, 10], 5: [7], 6: [10]},
            [[1, 2], [2, 3], [2, 4], [2, 5, 7], [4, 6, 10], [4, 10]],
        ),
        (
            {
                7: [10],
                10: [14],
                14: [3, 5, 18],
                5: [4],
                52: [13],
                4: [8],
                8: [14],
                18: [19],
                19: [31],
                31: [52],
            },
            [
                [7, 10, 14],
                [14, 3],
                [14, 5, 4, 8, 14],
                [14, 18, 19, 31, 52, 13],
            ],
        ),
        (
            {
                7: [3],
                3: [4],
                4: [8],
                8: [9],
                9: [7],
                1: [2],
                2: [5],
                5: [10],
                10: [2],
                16: [111],
                111: [16],
            },
            [[1, 2], [2, 5, 10, 2], [9, 7, 3, 4, 8, 9], [111, 16, 111]],
        ),
    ],
)
def test_maximal_non_branching_paths(
    graph: dict[int, list[int]], paths: list[list[int]]
) -> None:
    result = maximal_non_branching_paths(graph)
    assert len(result) == len(paths)
    actual = [
        sorted(path) if path[0] != path[-1] else sorted(path[:-1])
        for path in result
    ]
    expected = [
        sorted(path) if path[0] != path[-1] else sorted(path[:-1])
        for path in paths
    ]
    assert actual == expected


@pytest.mark.parametrize(
    "kmers, contigs",
    [
        (
            ["ATG", "ATG", "TGT", "TGG", "CAT", "GGA", "GAT", "AGA"],
            ["AGA", "ATG", "ATG", "CAT", "GAT", "TGGA", "TGT"],
        ),
        (["AG", "GT", "GC", "TA"], ["GTAG", "GC"]),
        (["GTT", "TTA", "TAC", "TTT"], ["GTT", "TTAC", "TTT"]),
        # (
        #     ["GAGA", "AGAG", "AACG", "ACGT", "ACGG"],
        #     ["ACGT", "ACGG", "AACG", "GAGAG"],
        # ),  # TODO: fix generate_contigs (cycle order)
        (
            ["TGAG", "GACT", "CTGA", "ACTG", "CTGA"],
            ["CTGA", "CTGA", "TGAG", "GACTG"],
        ),
    ],
)
def test_generate_contigs(kmers: list[str], contigs: list[str]) -> None:
    assert sorted(generate_contigs(kmers)) == sorted(contigs)
