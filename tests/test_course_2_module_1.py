from course_2.module_1 import (
    composition,
    de_bruijn_graph,
    de_bruijn_kgraph,
    genome_path,
    overlap_graph,
)


def test_composition() -> None:
    kmers = composition("CAATCCAAC", 5)
    assert kmers == ["CAATC", "AATCC", "ATCCA", "TCCAA", "CCAAC"]


def test_genome_path() -> None:
    genome = genome_path(["ACCGA", "CCGAA", "CGAAG", "GAAGC", "AAGCT"])
    assert genome == "ACCGAAGCT"


def test_overlap_graph() -> None:
    adj_list = overlap_graph(
        ["ATGCG", "GCATG", "CATGC", "AGGCA", "GGCAT", "GGCAC"]
    )
    assert adj_list == {
        "CATGC": {"ATGCG"},
        "GCATG": {"CATGC"},
        "GGCAT": {"GCATG"},
        "AGGCA": {"GGCAC", "GGCAT"},
    }


def test_de_bruijn_kgraph() -> None:
    adj_list = de_bruijn_kgraph("AAGATTCTCTAAGA", 4)
    assert adj_list == {
        "AAG": ["AGA", "AGA"],
        "AGA": ["GAT"],
        "ATT": ["TTC"],
        "CTA": ["TAA"],
        "CTC": ["TCT"],
        "GAT": ["ATT"],
        "TAA": ["AAG"],
        "TCT": ["CTA", "CTC"],
        "TTC": ["TCT"],
    }


def test_de_bruijn_graph() -> None:
    adj_list = de_bruijn_graph(
        ["GAGG", "CAGG", "GGGG", "GGGA", "CAGG", "AGGG", "GGAG"]
    )
    assert adj_list == {
        "AGG": ["GGG"],
        "CAG": ["AGG", "AGG"],
        "GAG": ["AGG"],
        "GGA": ["GAG"],
        "GGG": ["GGA", "GGG"],
    }
