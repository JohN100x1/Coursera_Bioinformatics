from collections import defaultdict, deque
from enum import IntEnum
from typing import Sequence, Iterable, Generator

from course_1.module_1 import reverse_complement


class ColourEnum(IntEnum):
    BLUE = 0
    RED = 1


Edge = tuple[int, int]
ColouredEdge = tuple[int, int, ColourEnum]


def chromosome_to_cycle(chromosome: Sequence[int]) -> list[int]:
    """Returns a list of integer graph nodes for chromosome."""
    nodes = [0] * (2 * len(chromosome))
    for j, i in enumerate(chromosome):
        if i > 0:
            nodes[2 * j] = 2 * i - 1
            nodes[2 * j + 1] = 2 * i
        else:
            nodes[2 * j] = -2 * i
            nodes[2 * j + 1] = -2 * i - 1
    return nodes


def cycle_to_chromosome(nodes: Sequence[int]) -> list[int]:
    """Returns chromosome for a list of integer graph nodes."""
    chromosome = [0] * (len(nodes) // 2)
    for j in range(len(nodes) // 2):
        if nodes[2 * j] < nodes[2 * j + 1]:
            chromosome[j] = nodes[2 * j + 1] // 2
        else:
            chromosome[j] = -nodes[2 * j] // 2
    return chromosome


def genome_to_edges(genome: Iterable[Sequence[int]]) -> set[Edge]:
    """Returns a list of coloured edges of the graph of genome."""
    edges = set()
    for chromosome in genome:
        nodes = chromosome_to_cycle(chromosome)
        for j in range(len(chromosome) - 1):
            edges.add((nodes[2 * j + 1], nodes[2 * j + 2]))
        edges.add((nodes[-1], nodes[0]))
    return edges


def edges_to_genome(edges: set[Edge]) -> list[list[int]]:
    """Returns a genome for a list of edges in genome graph."""

    def next_node(node: int) -> int:
        return node - 1 if node % 2 == 0 else node + 1

    def next_end_edge(end_node: int) -> tuple[int, int, Edge] | None:
        next_start = next_node(end_node)
        for edge in edges:
            if edge[0] == next_start:
                return edge[0], edge[1], edge
            elif edge[1] == next_start:
                return edge[1], edge[0], edge
        return None

    cycles: list[deque[int]] = []
    while edges:
        root = min(edges, key=lambda x: x[0])
        edges.remove(root)
        cycle_group = deque(root)

        next_edge_result = next_end_edge(root[1])
        if next_edge_result is not None:
            start, end, next_edge = next_edge_result
            edges.remove(next_edge)
            cycle_group.extend([start, end])
            while next_node(end) != root[0]:
                start, end, next_edge = next_end_edge(end)
                edges.remove(next_edge)
                cycle_group.extend([start, end])
        cycles.append(cycle_group)

    genome = []
    for cycle in cycles:
        cycle.appendleft(cycle[-1])
        genome.append(cycle_to_chromosome(cycle))
    return sorted(genome, key=lambda x: abs(x[0]))


def two_break_cycles(
    genome1: Iterable[Sequence[int]], genome2: Iterable[Sequence[int]]
) -> int:
    """
    Returns the number cycles between two genomes.
    The genome sequences must be the same size.
    """

    graph: dict[int, set[int]] = defaultdict(set)
    edges = genome_to_edges(genome1) | genome_to_edges(genome2)
    for u, v in edges:
        graph[u].add(v)
        graph[v].add(u)

    cycles = 0
    visited = set()
    while graph:
        start = next(iter(graph))
        if start in visited:
            continue
        cycle = {start}

        node = next((n for n in cycle if n in graph), None)
        while node is not None:
            while True:
                next_node = graph[node].pop()
                while graph[node] and next_node in cycle:
                    next_node = graph[node].pop()
                if not graph[node] - cycle:
                    graph.pop(node)
                node = next_node
                if node in cycle:
                    break
                cycle.add(node)
            node = next((n for n in cycle if n in graph), None)

        visited.update(cycle)
        cycles += 1
    return cycles


def two_break_dist(
    genome1: Iterable[Sequence[int]], genome2: Iterable[Sequence[int]]
) -> int:
    """Returns the 2-break distance between two genomes."""
    blocks = sum(len(cycle) for cycle in genome1)
    cycles = two_break_cycles(genome1, genome2)
    return blocks - cycles


def two_break_on_edges(
    edges: set[Edge], i1: int, i2: int, i3: int, i4: int
) -> set[Edge]:
    """
    Returns a list of edges of genome graph transformed by
    2-break(i1, i2, i3, i4).
    """
    if (i1, i2) in edges:
        edges.discard((i1, i2))
        edges.add((i1, i3))
    else:
        edges.remove((i2, i1))
        edges.add((i3, i1))
    if (i3, i4) in edges:
        edges.remove((i3, i4))
        edges.add((i2, i4))
    else:
        edges.remove((i4, i3))
        edges.add((i4, i2))
    return edges


def two_break_on_genome(
    genome: Iterable[Sequence[int]], i1: int, i2: int, i3: int, i4: int
) -> list[list[int]]:
    """Returns the genome transformed by 2-break(i1, i2, i3, i4)."""
    edges = genome_to_edges(genome)
    edges = two_break_on_edges(edges, i1, i2, i3, i4)
    return edges_to_genome(edges)


def next_nontrivial_cycle(
    edges: set[ColouredEdge],
) -> tuple[set[ColouredEdge], set[ColouredEdge]]:
    """Returns the next non-trivial cycle set of edges."""

    def next_end_edge(end_node: int) -> tuple[int, ColouredEdge]:
        for edge in edges:
            if edge[0] == end_node:
                return edge[1], edge
            elif edge[1] == end_node:
                return edge[0], edge

    remaining_edges = set()
    while edges:
        root = min(edges, key=lambda x: x[0])
        edges.remove(root)
        cycle = {root}

        end, next_edge = next_end_edge(root[1])
        edges.remove(next_edge)
        cycle.add(next_edge)

        if end == root[0]:
            remaining_edges.add(root)
            remaining_edges.add(next_edge)
            continue

        while end != root[0]:
            end, next_edge = next_end_edge(end)
            edges.remove(next_edge)
            cycle.add(next_edge)
        return remaining_edges | edges, cycle
    return remaining_edges | edges, set()


def coloured_edges(
    genome: Iterable[Sequence[int]], colour: ColourEnum
) -> set[ColouredEdge]:
    """Returns a list of coloured edges of the graph of genome."""
    edges = set()
    for chromosome in genome:
        nodes = chromosome_to_cycle(chromosome)
        for j in range(len(chromosome) - 1):
            edges.add((nodes[2 * j + 1], nodes[2 * j + 2], colour))
        edges.add((nodes[-1], nodes[0], colour))
    return edges


def two_break_on_coloured_edges(
    edges: set[ColouredEdge],
    colour: ColourEnum,
    i1: int,
    i2: int,
    i3: int,
    i4: int,
) -> set[ColouredEdge]:
    """
    Returns a list of edges of genome graph transformed by
    2-break(i1, i2, i3, i4).
    """
    if (i1, i2, colour) in edges:
        edges.discard((i1, i2, colour))
        edges.add((i1, i3, colour))
    else:
        edges.remove((i2, i1, colour))
        edges.add((i3, i1, colour))
    if (i3, i4, colour) in edges:
        edges.remove((i3, i4, colour))
        edges.add((i2, i4, colour))
    else:
        edges.remove((i4, i3, colour))
        edges.add((i4, i2, colour))
    return edges


def shortest_rearrangement_scenario(
    genome1: Iterable[Sequence[int]], genome2: Iterable[Sequence[int]]
) -> Generator[list[list[int]], None, None]:
    """Generates all genomes transformed by 2-breaks to another genome."""

    def next_red_node(node: int) -> int:
        for i, j, c in nontrivial_cycle:
            if c != ColourEnum.RED:
                continue
            if i == node:
                return j
            elif j == node:
                return i

    yield genome1
    edges_p = coloured_edges(genome1, ColourEnum.RED)
    edges_q = coloured_edges(genome2, ColourEnum.BLUE)
    edges = edges_p | edges_q
    trivial_cycles, nontrivial_cycle = next_nontrivial_cycle(edges)
    while nontrivial_cycle:
        i1, i3 = next(
            ((i, j) for i, j, c in nontrivial_cycle if c == ColourEnum.BLUE)
        )
        i2 = next_red_node(i1)
        i4 = next_red_node(i3)
        nontrivial_cycle = two_break_on_coloured_edges(
            nontrivial_cycle, ColourEnum.RED, i1, i2, i3, i4
        )
        edges = trivial_cycles | nontrivial_cycle
        red_edges = {(i, j) for i, j, c in edges if c == ColourEnum.RED}
        output = edges_to_genome(red_edges)
        yield output
        trivial_cycles, nontrivial_cycle = next_nontrivial_cycle(edges)


def shared_kmers(k: int, text1: str, text2: str) -> set[tuple[int, int]]:
    """Returns the starting positions of shared kmers in text1 and text2."""
    text1_rc = reverse_complement(text1)
    indexes = defaultdict(set)
    for i in range(len(text1) - k + 1):
        kmer = text1[i : i + k]
        indexes[kmer].add(i)

        kmer_rc = text1_rc[i : i + k]
        indexes[kmer_rc].add(len(text1) - k - i)

    positions = set()
    for j in range(len(text2) - k + 1):
        kmer = text2[j : j + k]
        if kmer not in indexes:
            continue
        for i in indexes[kmer]:
            positions.add((i, j))
    return positions
