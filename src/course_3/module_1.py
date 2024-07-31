from collections import deque, defaultdict
from enum import IntEnum
from itertools import accumulate
from typing import Hashable

INT_NEG_INFINITY = -0b10000000000000000000000000000000


class MoveEnum(IntEnum):
    STOP = 0
    DOWN = 1
    RIGHT = 2
    DIAGONAL = 3


def min_num_coins(target: int, coins: list[int]) -> int:
    """Get the minimum number of coins that sum up to target."""
    # TODO: limit len(min_coins) to max(coins)
    # TODO: return required coins that sum to target
    min_coins = [0] * (target + 1)
    for value in range(target + 1):
        num_coins = (1 + min_coins[value - c] for c in coins if value >= c)
        min_coins[value] = min(num_coins, default=0)
    return min_coins[target]


def manhattan_tourist(
    n: int, m: int, down: list[list[int]], right: list[list[int]]
) -> int:
    """Returns the longest path in the Manhattan Tourist Problem."""
    s = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        s[i][0] = s[i - 1][0] + down[i - 1][0]
    s[0][1 : m + 1] = list(accumulate(right[0]))

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            s[i][j] = max(
                s[i - 1][j] + down[i - 1][j], s[i][j - 1] + right[i][j - 1]
            )

    return s[n][m]


def backtrack_lcs(v: str, w: str) -> list[list[MoveEnum]]:
    """Returns the backtrack matrix for the lcs between v and w."""
    n, m = len(v) + 1, len(w) + 1
    s = [[0] * m for _ in range(n)]
    backtrack = [[MoveEnum.STOP] * m for _ in range(n)]

    for i in range(1, n):
        for j in range(1, m):
            match = 1 if v[i - 1] == w[j - 1] else 0
            prev = [
                (s[i - 1][j], MoveEnum.DOWN),
                (s[i][j - 1], MoveEnum.RIGHT),
                (s[i - 1][j - 1] + match, MoveEnum.DIAGONAL),
            ]
            s[i][j], backtrack[i][j] = max(prev, key=lambda x: x[0])
    return backtrack


def output_lcs(backtrack: list[list[MoveEnum]], v: str, w: str) -> str:
    """Returns the longest common subsequence between v_i and w_j."""
    lcs = []
    i, j = len(v), len(w)
    while i > 0 and j > 0:
        if backtrack[i][j] == MoveEnum.DOWN:
            i -= 1
        elif backtrack[i][j] == MoveEnum.RIGHT:
            j -= 1
        elif backtrack[i][j] == MoveEnum.DIAGONAL:
            lcs.append(v[i - 1])
            i -= 1
            j -= 1
        elif backtrack[i][j] == MoveEnum.STOP:
            break
        else:
            raise ValueError("Invalid backtrack matrix.")
    return "".join(reversed(lcs))


def longest_common_subseq(v: str, w: str) -> str:
    """Returns the longest common subsequence between v and w."""
    backtrack = backtrack_lcs(v, w)
    return output_lcs(backtrack, v, w)


def topological_sort[
    T: Hashable
](dag: dict[T, list[tuple[T, int]]]) -> list[T]:
    """Return a list of nodes from dag in topological order."""
    nodes = set(dag).union(set(v for nodes in dag.values() for v, _ in nodes))
    in_degree = defaultdict(int)
    for u in dag:
        for v, _ in dag[u]:
            in_degree[v] += 1

    queue = deque([v for v in nodes if in_degree[v] == 0])
    order = []

    while queue:
        u = queue.popleft()
        order.append(u)
        for v, _ in dag.get(u, []):
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)

    return order


def longest_path_dag[
    T: Hashable
](dag: dict[T, list[tuple[T, int]]], start: T, end: T) -> tuple[int, list[T]]:
    """Returns the longest path in weighted DAG with path."""
    topological_order = topological_sort(dag)

    dist = defaultdict(lambda: INT_NEG_INFINITY)
    dist[start] = 0

    predecessor = defaultdict(lambda: -1)

    for u in topological_order:
        if dist[u] == INT_NEG_INFINITY:
            continue
        for v, weight in dag.get(u, []):
            if dist[u] + weight > dist[v]:
                dist[v] = dist[u] + weight
                predecessor[v] = u

    # Reconstruct path from end node
    max_path = []
    end_node = end
    while end_node != -1:
        max_path.append(end_node)
        end_node = predecessor[end_node]
    max_path.reverse()

    return dist[end], max_path
