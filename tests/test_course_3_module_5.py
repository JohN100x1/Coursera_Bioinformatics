from course_3.module_5 import (
    chromosome_to_cycle,
    genome_to_edges,
    cycle_to_chromosome,
    edges_to_genome,
    two_break_dist,
    two_break_on_edges,
    two_break_on_genome,
    shortest_rearrangement_scenario,
    shared_kmers,
)


def test_chromosome_to_cycle() -> None:
    assert chromosome_to_cycle([+1, -2, -3, +4]) == [1, 2, 4, 3, 6, 5, 7, 8]


def test_cycle_to_chromosome() -> None:
    assert cycle_to_chromosome([1, 2, 4, 3, 6, 5, 7, 8]) == [+1, -2, -3, +4]


def test_coloured_edges() -> None:
    edges = genome_to_edges([[+1, -2, -3], [+4, +5, -6]])
    assert edges == {(2, 4), (3, 6), (5, 1), (8, 9), (10, 12), (11, 7)}


def test_edges_to_genome() -> None:
    edges = {(2, 4), (3, 6), (5, 1), (7, 9), (10, 12), (11, 8)}
    assert edges_to_genome(edges) == [[+1, -2, -3], [-4, +5, -6]]


def test_two_break_dist() -> None:
    dist = two_break_dist([[1, 2, 3, 4, 5, 6]], [[1, -3, -6, -5], [2, -4]])
    assert dist == 3


def test_two_break_on_edges() -> None:
    edges = two_break_on_edges({(2, 4), (3, 8), (7, 5), (6, 1)}, 1, 6, 3, 8)
    assert edges == {(2, 4), (3, 1), (7, 5), (6, 8)}


def test_two_break_on_genome() -> None:
    genome = two_break_on_genome([[+1, -2, -4, +3]], 1, 6, 3, 8)
    assert genome == [[+1, -2], [+3, -4]]  # TODO: forced [[+1, -2], [-3, +4]]


def test_shortest_rearrangement_scenario() -> None:
    genome1 = [[+1, -2, -3, +4]]
    genome2 = [[+1, +2, -4, -3]]
    dist = 3
    genome_gen = shortest_rearrangement_scenario(genome1, genome2)
    for i, genome in enumerate(genome_gen):
        assert two_break_dist(genome, genome2) == dist - i


def test_shared_kmers() -> None:
    positions = shared_kmers(3, "AAACTCATC", "TTTCAAATC")
    assert positions == {(0, 4), (0, 0), (4, 2), (6, 6)}
