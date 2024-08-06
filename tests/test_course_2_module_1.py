import pytest

from course_2.module_1 import (
    composition,
    de_bruijn_graph,
    de_bruijn_kgraph,
    genome_path,
    overlap_graph,
)


@pytest.mark.parametrize(
    "text, k, kmers",
    [
        ("CAATCCAAC", 5, ["CAATC", "AATCC", "ATCCA", "TCCAA", "CCAAC"]),
        ("TCGAA", 3, ["TCG", "CGA", "GAA"]),
        ("CCCCCCC", 2, ["CC", "CC", "CC", "CC", "CC", "CC"]),
        ("ACGT", 4, ["ACGT"]),
        (
            "GGGGGGTGGG",
            3,
            ["GGG", "GGG", "GGG", "GGG", "GGT", "GTG", "TGG", "GGG"],
        ),
    ],
)
def test_composition(text: str, k: int, kmers: list[str]) -> None:
    assert composition(text, k) == kmers


@pytest.mark.parametrize(
    "path, genome",
    [
        (["ACCGA", "CCGAA", "CGAAG", "GAAGC", "AAGCT"], "ACCGAAGCT"),
        (["CTT", "TTT", "TTG"], "CTTTG"),
        (["TT", "TG", "GT", "TT"], "TTGTT"),
        (
            [
                "AGCAGATC",
                "GCAGATCA",
                "CAGATCAT",
                "AGATCATC",
                "GATCATCG",
                "ATCATCGG",
            ],
            "AGCAGATCATCGG",
        ),
    ],
)
def test_genome_path(path: list[str], genome: str) -> None:
    assert genome_path(path) == genome


@pytest.mark.parametrize(
    "kmers, graph",
    [
        (
            ["ATGCG", "GCATG", "CATGC", "AGGCA", "GGCAT", "GGCAC"],
            {
                "CATGC": {"ATGCG"},
                "GCATG": {"CATGC"},
                "GGCAT": {"GCATG"},
                "AGGCA": {"GGCAC", "GGCAT"},
            },
        ),
        (
            ["AT", "CA", "GG", "GT", "TG"],
            {
                "AT": {"TG"},
                "CA": {"AT"},
                "GG": {"GG", "GT"},
                "GT": {"TG"},
                "TG": {"GG", "GT"},
            },
        ),
        (["ATG", "TGA"], {"ATG": {"TGA"}}),
        (
            ["AA", "AC", "AG", "AT", "CA", "GT", "TA"],
            {
                "AA": {"AA", "AC", "AG", "AT"},
                "AC": {"CA"},
                "AT": {"TA"},
                "AG": {"GT"},
                "CA": {"AA", "AC", "AG", "AT"},
                "GT": {"TA"},
                "TA": {"AA", "AC", "AG", "AT"},
            },
        ),
    ],
)
def test_overlap_graph(kmers: list[str], graph: dict[str, set[str]]) -> None:
    assert overlap_graph(kmers) == graph


@pytest.mark.parametrize(
    "text, k, graph",
    [
        (
            "AAGATTCTCTAAGA",
            4,
            {
                "AAG": ["AGA", "AGA"],
                "AGA": ["GAT"],
                "ATT": ["TTC"],
                "CTA": ["TAA"],
                "CTC": ["TCT"],
                "GAT": ["ATT"],
                "TAA": ["AAG"],
                "TCT": ["CTC", "CTA"],
                "TTC": ["TCT"],
            },
        ),
        (
            "ACGTGTATA",
            3,
            {
                "AC": ["CG"],
                "CG": ["GT"],
                "GT": ["TG", "TA"],
                "TG": ["GT"],
                "TA": ["AT"],
                "AT": ["TA"],
            },
        ),
        ("AGCCT", 4, {"AGC": ["GCC"], "GCC": ["CCT"]}),
        ("CCTCCG", 3, {"CC": ["CT", "CG"], "CT": ["TC"], "TC": ["CC"]}),
        (
            "GCTTCTTC",
            4,
            {
                "GCT": ["CTT"],
                "CTT": ["TTC", "TTC"],
                "TTC": ["TCT"],
                "TCT": ["CTT"],
            },
        ),
        (
            "TTTTTTTTTT",
            5,
            {"TTTT": ["TTTT", "TTTT", "TTTT", "TTTT", "TTTT", "TTTT"]},
        ),
    ],
)
def test_de_bruijn_kgraph(
    text: str, k: int, graph: dict[str, list[str]]
) -> None:
    assert de_bruijn_kgraph(text, k) == graph


@pytest.mark.parametrize(
    "kmers, graph",
    [
        (
            ["GAGG", "CAGG", "GGGG", "GGGA", "CAGG", "AGGG", "GGAG"],
            {
                "AGG": ["GGG"],
                "CAG": ["AGG", "AGG"],
                "GAG": ["AGG"],
                "GGA": ["GAG"],
                "GGG": ["GGG", "GGA"],
            },
        ),
        (
            ["GCAAG", "CAGCT", "TGACG"],
            {"GCAA": ["CAAG"], "CAGC": ["AGCT"], "TGAC": ["GACG"]},
        ),
        (["AGGT", "GGCT", "AGGC"], {"AGG": ["GGT", "GGC"], "GGC": ["GCT"]}),
        (
            ["TTCT", "GGCT", "AAGT", "GGCT", "TTCT"],
            {"TTC": ["TCT", "TCT"], "GGC": ["GCT", "GCT"], "AAG": ["AGT"]},
        ),
        (
            ["CA", "CA", "CA", "CA", "CC", "CA"],
            {"C": ["A", "A", "A", "A", "C", "A"]},
        ),
    ],
)
def test_de_bruijn_graph(
    kmers: list[str], graph: dict[str, list[str]]
) -> None:
    assert de_bruijn_graph(kmers) == graph
