def pattern_matching(pattern: str, genome: str) -> list[int]:
    """Returns a list of starting indexes for pattern in genome."""
    k = len(pattern)
    return [
        i for i in range(len(genome) - k + 1) if genome[i : i + k] == pattern
    ]
