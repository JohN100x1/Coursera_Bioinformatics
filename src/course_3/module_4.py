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


if __name__ == "__main__":
    txt = "+6 -12 -9 +17 +18 -4 +5 -3 +11 +19 +14 +10 +8 +15 -13 +20 +2 +7 -16 -1"
    print(len(list(greedy_sorting([int(x) for x in txt.split(" ")]))))
    txt = "+6 -12 -9 +17 +18 -4 +5 -3 +11 +19 +20 +10 +8 +15 -14 -13 +2 +7 -16 -1"
    print(count_breakpoints([int(x) for x in txt.split(" ")]))
