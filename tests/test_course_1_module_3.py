from course_1.module_3 import (
    dna_hamming_distance,
    greedy_motif_search,
    improved_greedy_motif_search,
    median_strings,
    motif_enumeration,
    profile_probable_kmer,
)


def test_motif_enumeration() -> None:
    patterns = motif_enumeration(
        ["ATTTGGC", "TGCCTTA", "CGGTATC", "GAAAATT"], 3, 1
    )
    assert patterns == {"ATT", "ATA", "TTT", "GTT"}


def test_dna_hamming_distance() -> None:
    distance = dna_hamming_distance(
        "AAA",
        ["TTACCTTAAC", "GATATCTGTC", "ACGGCGTTCG", "CCCTAAAGAG", "CGTCAGAGGT"],
    )
    assert distance == 5


def test_median_string() -> None:
    pattern = median_strings(
        [
            "AAATTGACGCAT",
            "GACGACCACGTT",
            "CGTCAGCGCCTG",
            "GCTGAGCACCGG",
            "AGTTCGGGACAG",
        ],
        3,
    )
    assert pattern == ["GAC"]


def test_profile_probable_kmer() -> None:
    pattern = profile_probable_kmer(
        "ACCTGTTTATTGCCTAAGTTCCGAACAAACCCAATATAGCCCGAGGGCCT",
        5,
        [
            [0.2, 0.2, 0.3, 0.2, 0.3],
            [0.4, 0.3, 0.1, 0.5, 0.1],
            [0.3, 0.3, 0.5, 0.2, 0.4],
            [0.1, 0.2, 0.1, 0.1, 0.2],
        ],
    )
    assert pattern == "CCGAG"


def test_greedy_motif_search() -> None:
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
    )
    assert motifs == ["CAG", "CAG", "CAA", "CAA", "CAA"]


def test_improved_greedy_motif_search() -> None:
    motifs = improved_greedy_motif_search(
        [
            "GGCGTTCAGGCA",
            "AAGAATCAGTCA",
            "CAAGGAGTTCGC",
            "CACGTCAATCAC",
            "CAATAATATTCG",
        ],
        3,
        5,
    )
    assert motifs == ["TTC", "ATC", "TTC", "ATC", "TTC"]
