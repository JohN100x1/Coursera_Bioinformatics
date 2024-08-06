from random import seed

import pytest

from course_1.module_4 import (
    repeated_gibbs_sampler,
    repeated_random_motif_search,
)


@pytest.mark.skip(reason="Randomised test")
@pytest.mark.parametrize(
    "dna, k, t, motifs",
    [
        (
            [
                "CGCCCCTCTCGGGGGTGTTCAGTAAACGGCCA",
                "GGGCGAGGTATGTGTAAGTGCCAAGGTGCCAG",
                "TAGTACCGAGACCGAAAGAAGTATACAGGCGT",
                "TAGATCAAGTTTCAGGTGCACGTCGGTGAACC",
                "AATCCACCAGCTCCACGTGCAATGTTGGCCTA",
            ],
            8,
            5,
            [
                "TCTCGGGG",
                "CCAAGGTG",
                "TACAGGCG",
                "TTCAGGTG",
                "TCCACGTG",
            ],
        ),
        (
            [
                "AATTGGCACATCATTATCGATAACGATTCGCCGCATTGCC",
                "GGTTAACATCGAATAACTGACACCTGCTCTGGCACCGCTC",
                "AATTGGCGGCGGTATAGCCAGATAGTGCCAATAATTTCCT",
                "GGTTAATGGTGAAGTGTGGGTTATGGGGAAAGGCAGACTG",
                "AATTGGACGGCAACTACGGTTACAACGCAGCAAGAATATT",
                "GGTTAACTGTTGTTGCTAACACCGTTAAGCGACGGCAACT",
                "AATTGGCCAACGTAGGCGCGGCTTGGCATCTCGGTGTGTG",
                "GGTTAAAAGGCGCATCTTACTCTTTTCGCTTTCAAAAAAA",
            ],
            6,
            8,
            [
                "CGATAA",
                "GGTTAA",
                "GGTATA",
                "GGTTAA",
                "GGTTAC",
                "GGTTAA",
                "GGCCAA",
                "GGTTAA",
            ],
        ),
        (
            [
                "GCACATCATTAAACGATTCGCCGCATTGCCTCGATTAACC",
                "TCATAACTGACACCTGCTCTGGCACCGCTCATCCAAGGCC",
                "AAGCGGGTATAGCCAGATAGTGCCAATAATTTCCTTAACC",
                "AGTCGGTGGTGAAGTGTGGGTTATGGGGAAAGGCAAGGCC",
                "AACCGGACGGCAACTACGGTTACAACGCAGCAAGTTAACC",
                "AGGCGTCTGTTGTTGCTAACACCGTTAAGCGACGAAGGCC",
                "AAGCTTCCAACATCGTCTTGGCATCTCGGTGTGTTTAACC",
                "AATTGAACATCTTACTCTTTTCGCTTTCAAAAAAAAGGCC",
            ],
            6,
            8,
            [
                "TTAACC",
                "ATAACT",
                "TTAACC",
                "TGAAGT",
                "TTAACC",
                "TTAAGC",
                "TTAACC",
                "TGAACA",
            ],
        ),
    ],
)
def test_repeated_random_motif_search(
    dna: list[str], k: int, t: int, motifs: list[str]
) -> None:
    seed(0)
    assert repeated_random_motif_search(dna, k, t, 1000) == motifs


@pytest.mark.skip(reason="Randomised test")
def test_gibbs_sample() -> None:
    seed(1)
    motifs = repeated_gibbs_sampler(
        [
            "CGCCCCTCTCGGGGGTGTTCAGTAACCGGCCA",
            "GGGCGAGGTATGTGTAAGTGCCAAGGTGCCAG",
            "TAGTACCGAGACCGAAAGAAGTATACAGGCGT",
            "TAGATCAAGTTTCAGGTGCACGTCGGTGAACC",
            "AATCCACCAGCTCCACGTGCAATGTTGGCCTA",
        ],
        8,
        5,
        100,
        20,
    )
    assert motifs == [
        "TCTCGGGG",
        "CCAAGGTG",
        "TACAGGCG",
        "TTCAGGTG",
        "TCCACGTG",
    ]
