from typing import Generator


def greedy_sorting(perm: list[int]) -> Generator[list[int], None, None]:
    """Returns the sorted permutation using greedy sorting."""
    reversal_dist = 0
    n = len(perm)
    for k in range(1, len(perm) + 1):
        if perm[k - 1] not in {k, -k}:
            k_idx: int
            for idx in range(k, n):
                if perm[idx] in {k, -k}:
                    k_idx = idx
                    break
            else:
                raise ValueError(f"{k} or {-k} not found in perm.")
            perm = (
                perm[: k - 1]
                + [-1 * x for x in reversed(perm[k - 1 : k_idx + 1])]
                + perm[k_idx + 1 :]
            )
            reversal_dist += 1
            yield perm
        if perm[k - 1] == -k:
            perm[k - 1] = k
            reversal_dist += 1
            yield perm


def count_breakpoints(perm: list[int]) -> int:
    """Returns the number of break points in permutation."""
    count = sum(perm[i + 1] - perm[i] != 1 for i in range(len(perm) - 1))
    if perm[0] != 1:
        count += 1
    if len(perm) - perm[-1] != 0:
        count += 1
    return count
