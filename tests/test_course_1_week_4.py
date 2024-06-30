from random import seed

from course_1.week_4 import (
    repeated_gibbs_sampler,
    repeated_random_motif_search,
)


def test_repeated_random_motif_search() -> None:
    seed(0)
    motifs = repeated_random_motif_search(
        [
            "CGCCCCTCTCGGGGGTGTTCAGTAAACGGCCA",
            "GGGCGAGGTATGTGTAAGTGCCAAGGTGCCAG",
            "TAGTACCGAGACCGAAAGAAGTATACAGGCGT",
            "TAGATCAAGTTTCAGGTGCACGTCGGTGAACC",
            "AATCCACCAGCTCCACGTGCAATGTTGGCCTA",
        ],
        8,
        5,
        1000,
    )
    assert motifs == [
        "TCTCGGGG",
        "CCAAGGTG",
        "TACAGGCG",
        "TTCAGGTG",
        "TCCACGTG",
    ]


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
