from collections import defaultdict


def composition(text: str, k: int) -> list[str]:
    """Returns a list of k-mers which are substrings of text."""
    return [text[i : i + k] for i in range(len(text) - k + 1)]


def genome_path(kmers: list[str]) -> str:
    """Returns the genome from a list of kmers."""
    return kmers[0] + "".join(kmer[-1] for kmer in kmers[1:])


def overlap_graph(kmers: list[str]) -> dict[str, set[str]]:
    """Returns an adjacency list for the overlap graph of kmers."""
    adj_list = defaultdict(set)
    prefix_dict = defaultdict(set)
    for kmer in kmers:
        prefix_dict[kmer[:-1]].add(kmer)
    for kmer in kmers:
        suffix = kmer[1:]
        if suffix in prefix_dict:
            adj_list[kmer].update(prefix_dict[suffix])
    return adj_list


def de_bruijn_kgraph(text: str, k: int) -> dict[str, list[str]]:
    """Returns the De Bruijn graph adjacency list for a given text."""
    adj_list = defaultdict(list)
    k -= 1
    kmer = text[:k]
    for i in range(1, len(text) - k + 1):
        adj_kmer = text[i : i + k]
        adj_list[kmer].append(adj_kmer)
        kmer = adj_kmer
    return dict(adj_list)


def de_bruijn_graph(kmers: list[str]) -> dict[str, list[str]]:
    """Returns the De Bruijn graph adjacency list for a list of kmers."""
    adj_list = defaultdict(list)
    for kmer in kmers:
        adj_list[kmer[:-1]].append(kmer[1:])
    return dict(adj_list)
