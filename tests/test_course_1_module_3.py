import pytest

from course_1.module_3 import (
    dna_hamming_distance,
    greedy_motif_search,
    median_strings,
    motif_enumeration,
    profile_probable_kmer,
)


@pytest.mark.parametrize(
    "dna, k, d, patterns",
    [
        (
            ["ATTTGGC", "TGCCTTA", "CGGTATC", "GAAAATT"],
            3,
            1,
            {"ATT", "ATA", "TTT", "GTT"},
        ),
        (["ACGT", "ACGT", "ACGT"], 3, 0, {"ACG", "CGT"}),
        (
            ["AAAAA", "AAAAA", "AAAAA"],
            3,
            1,
            {
                "TAA",
                "AAG",
                "CAA",
                "ATA",
                "AAC",
                "GAA",
                "AAA",
                "AGA",
                "AAT",
                "ACA",
            },
        ),
        (
            ["AAAAA", "AAAAA", "AAAAA"],
            3,
            3,
            {
                "CTG",
                "ATG",
                "AAG",
                "TAC",
                "TGA",
                "GTG",
                "ATA",
                "CCC",
                "TCT",
                "AGA",
                "TTA",
                "GTA",
                "GCA",
                "TGG",
                "CCA",
                "CGC",
                "TCA",
                "CTC",
                "AGC",
                "CGT",
                "AAC",
                "GCT",
                "CAG",
                "TGT",
                "GGT",
                "CAT",
                "TGC",
                "GCG",
                "CCT",
                "GGG",
                "TCG",
                "GAA",
                "GCC",
                "ATC",
                "ATT",
                "CAC",
                "CGG",
                "TAG",
                "GAC",
                "GAT",
                "GAG",
                "GGA",
                "TCC",
                "TAA",
                "CGA",
                "CCG",
                "AGG",
                "CAA",
                "GGC",
                "ACT",
                "TTG",
                "TTC",
                "AAA",
                "TTT",
                "GTT",
                "AAT",
                "ACA",
                "GTC",
                "AGT",
                "CTA",
                "TAT",
                "ACC",
                "ACG",
                "CTT",
            },
        ),
        (["AAAAA", "AAAAA", "AACAA"], 3, 0, set()),
        (["AACAA", "AAAAA", "AAAAA"], 3, 0, set()),
    ],
)
def test_motif_enumeration(
    dna: list[str], k: int, d: int, patterns: set[str]
) -> None:
    assert motif_enumeration(dna, k, d) == patterns


@pytest.mark.parametrize(
    "pattern, dna, dist",
    [
        (
            "AAA",
            [
                "TTACCTTAAC",
                "GATATCTGTC",
                "ACGGCGTTCG",
                "CCCTAAAGAG",
                "CGTCAGAGGT",
            ],
            5,
        ),
        ("TAA", ["TTTATTT", "CCTACAC", "GGTAGAG"], 3),
        ("AAA", ["AAACT", "AAAC", "AAAG"], 0),
        ("AAA", ["TTTTAAA", "CCCCAAA", "GGGGAAA"], 0),
        ("AAA", ["AAATTTT", "AAACCCC", "AAAGGGG"], 0),
    ],
)
def test_dna_hamming_distance(pattern: str, dna: list[str], dist: int) -> None:
    assert dna_hamming_distance(pattern, dna) == dist


@pytest.mark.parametrize(
    "dna, k, patterns",
    [
        (
            [
                "AAATTGACGCAT",
                "GACGACCACGTT",
                "CGTCAGCGCCTG",
                "GCTGAGCACCGG",
                "AGTTCGGGACAG",
            ],
            3,
            {"GAC"},
        ),
        (["ACGT", "ACGT", "ACGT"], 3, {"CGT", "ACG"}),
        (["ATA", "ACA", "AGA", "AAT", "AAC"], 3, {"AAA"}),
        (["AAG", "AAT"], 3, {"AAT", "AAG"}),
    ],
)
def test_median_string(dna: list[str], k: int, patterns: set[str]) -> None:
    assert median_strings(dna, k) == patterns


@pytest.mark.parametrize(
    "text, k, profile, pattern",
    [
        (
            "ACCTGTTTATTGCCTAAGTTCCGAACAAACCCAATATAGCCCGAGGGCCT",
            5,
            [
                [0.2, 0.2, 0.3, 0.2, 0.3],
                [0.4, 0.3, 0.1, 0.5, 0.1],
                [0.3, 0.3, 0.5, 0.2, 0.4],
                [0.1, 0.2, 0.1, 0.1, 0.2],
            ],
            "CCGAG",
        ),
        (
            "AGCAGCTTTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATCTGAA"
            "CTGGTTACCTGCCGTGAGTAAAT",
            8,
            [
                [0.7, 0.2, 0.1, 0.5, 0.4, 0.3, 0.2, 0.1],
                [0.2, 0.2, 0.5, 0.4, 0.2, 0.3, 0.1, 0.6],
                [0.1, 0.3, 0.2, 0.1, 0.2, 0.1, 0.4, 0.2],
                [0.0, 0.3, 0.2, 0.0, 0.2, 0.3, 0.3, 0.1],
            ],
            "AGCAGCTT",
        ),
        (
            "TTACCATGGGACCGCTGACTGATTTCTGGCGTCAGCGTGATGCTGGTGTGGATGACATTCCGGTG"
            "CGCTTTGTAAGCAGAGTTTA",
            12,
            [
                [0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.1, 0.2, 0.3, 0.4, 0.5],
                [0.3, 0.2, 0.1, 0.1, 0.2, 0.1, 0.1, 0.4, 0.3, 0.2, 0.2, 0.1],
                [0.2, 0.1, 0.4, 0.3, 0.1, 0.1, 0.1, 0.3, 0.1, 0.1, 0.2, 0.1],
                [0.3, 0.4, 0.1, 0.1, 0.1, 0.1, 0.0, 0.2, 0.4, 0.4, 0.2, 0.3],
            ],
            "AAGCAGAGTTTA",
        ),
        (
            "TGCCCGAGCTATCTTATGCGCATCGCATGCGGACCCTTCCCTAGGCTTGTCGCAAGCCATTATCC"
            "TGGGCGCTAGTTGCGCGAGTATTGTCAGACCTGATGACGCTGTAAGCTAGCGTGTTCAGCGGCGC"
            "GCAATGAGCGGTTTAGATCACAGAATCCTTTGGCGTATTCCTATCCGTTACATCACCTTCCTCAC"
            "CCCTA",
            6,
            [
                [0.364, 0.333, 0.303, 0.212, 0.121, 0.242],
                [0.182, 0.182, 0.212, 0.303, 0.182, 0.303],
                [0.121, 0.303, 0.182, 0.273, 0.333, 0.303],
                [0.333, 0.182, 0.303, 0.212, 0.364, 0.152],
            ],
            "TGTCGC",
        ),
    ],
)
def test_profile_probable_kmer(
    text: str, k: int, profile: list[list[float]], pattern: str
) -> None:
    assert profile_probable_kmer(text, k, profile) == pattern


@pytest.mark.parametrize(
    "dna, k, t, motifs",
    [
        (
            [
                "GGCGTTCAGGCA",
                "AAGAATCAGTCA",
                "CAAGGAGTTCGC",
                "CACGTCAATCAC",
                "CAATAATATTCG",
            ],
            3,
            5,
            ["CAG", "CAG", "CAA", "CAA", "CAA"],
        ),
        (
            ["GCCCAA", "GGCCTG", "AACCTA", "TTCCTT"],
            3,
            4,
            ["GCC", "GCC", "AAC", "TTC"],
        ),
        (
            [
                "GAGGCGCACATCATTATCGATAACGATTCGCCGCATTGCC",
                "TCATCGAATCCGATAACTGACACCTGCTCTGGCACCGCTC",
                "TCGGCGGTATAGCCAGAAAGCGTAGTGCCAATAATTTCCT",
                "GAGTCGTGGTGAAGTGTGGGTTATGGGGAAAGGCAGACTG",
                "GACGGCAACTACGGTTACAACGCAGCAACCGAAGAATATT",
                "TCTGTTGTTGCTAACACCGTTAAAGGCGGCGACGGCAACT",
                "AAGCGGCCAACGTAGGCGCGGCTTGGCATCTCGGTGTGTG",
                "AATTGAAAGGCGCATCTTACTCTTTTCGCTTTCAAAAAAA",
            ],
            5,
            8,
            [
                "GAGGC",
                "TCATC",
                "TCGGC",
                "GAGTC",
                "GCAGC",
                "GCGGC",
                "GCGGC",
                "GCATC",
            ],
        ),
        (
            [
                "GCAGGTTAATACCGCGGATCAGCTGAGAAACCGGAATGTGCGT",
                "CCTGCATGCCCGGTTTGAGGAACATCAGCGAAGAACTGTGCGT",
                "GCGCCAGTAACCCGTGCCAGTCAGGTTAATGGCAGTAACATTT",
                "AACCCGTGCCAGTCAGGTTAATGGCAGTAACATTTATGCCTTC",
                "ATGCCTTCCGCGCCAATTGTTCGTATCGTCGCCACTTCGAGTG",
            ],
            6,
            5,
            ["GTGCGT", "GTGCGT", "GCGCCA", "GTGCCA", "GCGCCA"],
        ),
        (
            [
                "GACCTACGGTTACAACGCAGCAACCGAAGAATATTGGCAA",
                "TCATTATCGATAACGATTCGCCGGAGGCCATTGCCGCACA",
                "GGAGTCTGGTGAAGTGTGGGTTATGGGGCAGACTGGGAAA",
                "GAATCCGATAACTGACACCTGCTCTGGCACCGCTCTCATC",
                "AAGCGCGTAGGCGCGGCTTGGCATCTCGGTGTGTGGCCAA",
                "AATTGAAAGGCGCATCTTACTCTTTTCGCTTAAAATCAAA",
                "GGTATAGCCAGAAAGCGTAGTTAATTTCGGCTCCTGCCAA",
                "TCTGTTGTTGCTAACACCGTTAAAGGCGGCGACGGCAACT",
            ],
            5,
            8,
            [
                "GCAGC",
                "TCATT",
                "GGAGT",
                "TCATC",
                "GCATC",
                "GCATC",
                "GGTAT",
                "GCAAC",
            ],
        ),
    ],
)
def test_greedy_motif_search(
    dna: list[str], k: int, t: int, motifs: list[str]
) -> None:
    assert greedy_motif_search(dna, k, t) == motifs


def test_improved_greedy_motif_search() -> None:
    motifs = greedy_motif_search(
        [
            "GGCGTTCAGGCA",
            "AAGAATCAGTCA",
            "CAAGGAGTTCGC",
            "CACGTCAATCAC",
            "CAATAATATTCG",
        ],
        3,
        5,
        True,
    )
    assert motifs == ["TTC", "ATC", "TTC", "ATC", "TTC"]
