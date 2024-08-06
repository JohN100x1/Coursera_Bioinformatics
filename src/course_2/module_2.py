from collections import defaultdict
from itertools import product
from random import choice, randint
from typing import Hashable

from course_2.module_1 import de_bruijn_graph, genome_path

type pair = tuple[str, str]


def count_in_degrees[T: Hashable](adj_list: dict[T, list[T]]) -> dict[T, int]:
    """Returns the in-degrees of an adjacency list."""
    in_degrees: dict[T, int] = defaultdict(int)
    for node, neighbors in adj_list.items():
        assert in_degrees[node] >= 0  # Ensures node exists in dict
        for neighbour in neighbors:
            in_degrees[neighbour] += 1
    return dict(in_degrees)


def count_out_degrees[T: Hashable](adj_list: dict[T, list[T]]) -> dict[T, int]:
    """Returns the out-degrees of an adjacency list."""
    nodes = set()
    for u, neighbors in adj_list.items():
        nodes.add(u)
        nodes.update(neighbors)
    return {node: len(adj_list.get(node, [])) for node in nodes}


def eulerian_cycle[
    T: Hashable
](adj_list: dict[T, list[T]], start: T | None = None) -> list[T]:
    """Return an Eulerian cycle for the given graph."""

    def get_next_node(node: T) -> T:
        next_node = adj_list[node].pop(randint(0, len(adj_list[node]) - 1))
        if not adj_list[node]:
            adj_list.pop(node)
        return next_node

    if start is None:
        start = choice(list(adj_list))
    cycle = [start]

    while adj_list:
        current_node = next((node for node in cycle if node in adj_list), None)
        if current_node is None:
            break
        new_cycle = []
        while True:
            new_cycle.append(current_node)
            if current_node not in adj_list:
                raise ValueError(f"{current_node} has no edges")
            current_node = get_next_node(current_node)
            if current_node == new_cycle[0]:
                new_cycle.append(current_node)
                break
        splice_index = cycle.index(new_cycle[0])
        cycle = cycle[:splice_index] + new_cycle + cycle[splice_index + 1 :]
    return cycle


def eulerian_path[T: Hashable](adj_list: dict[T, list[T]]) -> list[T]:
    """Return an Eulerian path for a nearly balanced graph."""
    in_degrees = count_in_degrees(adj_list)
    out_degrees = count_out_degrees(adj_list)
    nodes = set(in_degrees).union(out_degrees)
    unbalanced_nodes = [u for u in nodes if in_degrees[u] != out_degrees[u]]

    if len(unbalanced_nodes) < 2:
        return eulerian_cycle(adj_list, start=next(iter(adj_list)))
    if len(unbalanced_nodes) > 2:
        raise ValueError("Graph is not nearly balanced.")

    start, end = unbalanced_nodes[0], unbalanced_nodes[1]
    if (
        in_degrees[start] == out_degrees[start] + 1
        and in_degrees[end] + 1 == out_degrees[end]
    ):
        start, end = end, start
    if (
        in_degrees[end] + in_degrees[start]
        != out_degrees[end] + out_degrees[start]
    ):
        raise ValueError(f"Degree mismatch for nodes {start} and {end}")
    # Add extra edge to end
    if adj_list.get(end, None) is not None:
        adj_list[end].append(start)
    else:
        adj_list[end] = [start]
    # Traverse from end, then cutoff the edge from end to start
    cycle = eulerian_cycle(adj_list, start=end)
    for i in range(1, len(cycle)):
        if cycle[i - 1] == end and cycle[i] == start:
            return cycle[i:-1] + cycle[:i]
    raise ValueError(f"Edge {end} -> {start} does not exist.")


def string_reconstruction(kmers: list[str]) -> str:
    """Find the Eulerian path in the De Bruijn graph."""
    adj_list = de_bruijn_graph(kmers)
    path = eulerian_path(adj_list)
    return genome_path(path)


def k_universal_circular_string(k: int) -> str:
    """Returns the k-universal circular string."""
    kmers = ["".join(x) for x in product("01", repeat=k)]
    adj_list = de_bruijn_graph(kmers)
    cycle = eulerian_cycle(adj_list)
    return genome_path(cycle[:-1])[: (2 - k)]


def paired_composition(text: str, k: int, d: int) -> list[pair]:
    """Returns the paired (k, d)-mer composition of text."""
    return sorted(
        [
            (text[i : i + k], text[(i + k + d) : (i + d + 2 * k)])
            for i in range(len(text) - 2 * k - d + 1)
        ]
    )


def string_spelled_by_gapped_patterns(
    kmer_pairs: list[pair], k: int, d: int
) -> str:
    """Returns the string spelled by the list of (k, d)-mers."""
    prefix_string = genome_path([kmer for kmer, _ in kmer_pairs])
    suffix_string = genome_path([kmer for _, kmer in kmer_pairs])
    for i in range(k + d + 1, len(prefix_string)):
        if prefix_string[i] != suffix_string[i - k - d]:
            msg = (
                " " * 12
                + prefix_string
                + "-" * (k + d)
                + "\n"
                + " " * 12
                + "-" * (k + d)
                + suffix_string
            )
            raise ValueError(f"No string spelled by gapped patterns:\n{msg}")
    return prefix_string + suffix_string[-(k + d) :]


def paired_de_bruijn_graph(kmer_pairs: list[pair]) -> dict[pair, list[pair]]:
    """Returns the De Bruijn graph adjacency list for a list of kmer pairs."""
    adj_list = defaultdict(list)
    for kmer1, kmer2 in kmer_pairs:
        adj_list[(kmer1[:-1], kmer2[:-1])].append((kmer1[1:], kmer2[1:]))
    return {key: sorted(vals) for key, vals in adj_list.items()}


def paired_string_reconstruction(
    kmer_pairs: list[pair], k: int, d: int
) -> str:
    """Returns the string reconstruction for list of kmer pairs."""
    adj_list = paired_de_bruijn_graph(kmer_pairs)
    path = eulerian_path(adj_list)
    return string_spelled_by_gapped_patterns(path, k, d)


def maximal_non_branching_paths[
    T: Hashable
](adj_list: dict[T, list[T]]) -> list[list[T]]:
    """Returns a list non-branching paths in graph."""
    paths = []
    in_degrees_counts = count_in_degrees(adj_list)
    out_degrees_counts = count_out_degrees(adj_list)
    unexplored = set(in_degrees_counts.keys())
    for node in in_degrees_counts:
        if in_degrees_counts[node] == out_degrees_counts[node] == 1:
            continue
        if out_degrees_counts[node] == 0:
            continue
        for neighbour in adj_list[node]:
            path = [node, neighbour]
            while (
                in_degrees_counts[neighbour]
                == out_degrees_counts[neighbour]
                == 1
            ):
                neighbour = adj_list[neighbour][0]
                path.append(neighbour)
            paths.append(path)
            unexplored -= set(path)
    while unexplored:
        node = unexplored.pop()
        neighbour = adj_list[node][0]
        path = [node, neighbour]
        while neighbour != path[0]:
            neighbour = adj_list[neighbour][0]
            path.append(neighbour)
        paths.append(path)
        unexplored -= set(path)
    return paths


def generate_contigs(kmers: list[str]) -> list[str]:
    """Returns a list of contigs."""
    adj_list = de_bruijn_graph(kmers)
    paths = maximal_non_branching_paths(adj_list)
    return [genome_path(path) for path in paths]
