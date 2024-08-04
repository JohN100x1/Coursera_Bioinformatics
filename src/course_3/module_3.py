from collections import deque

from course_3.module_1 import INT_NEG_INFINITY, MoveEnum


def output_alignment_gap(
    backtrack: list[list[MoveEnum]],
    backtrack_lower: list[list[MoveEnum]],
    backtrack_upper: list[list[MoveEnum]],
    backtrack_middle: list[list[MoveEnum]],
    v: str,
    w: str,
    i: int,
    j: int,
) -> tuple[str, str]:
    """
    Returns the alignment of v and w using upper and lower backtracking
    matrices and (i, j)-start.
    """
    v_align = []
    w_align = []
    while i > 0 or j > 0:
        if backtrack[i][j] in {MoveEnum.DOWN, MoveEnum.TO_LOWER}:
            if backtrack[i][j] == MoveEnum.TO_LOWER:
                backtrack = backtrack_middle
            i -= 1
            v_align.append(v[i])
            w_align.append("-")
        elif backtrack[i][j] in {MoveEnum.RIGHT, MoveEnum.TO_UPPER}:
            if backtrack[i][j] == MoveEnum.TO_UPPER:
                backtrack = backtrack_middle
            j -= 1
            v_align.append("-")
            w_align.append(w[j])
        elif backtrack[i][j] == MoveEnum.DOWN_RIGHT:
            i -= 1
            j -= 1
            v_align.append(v[i])
            w_align.append(w[j])
        elif backtrack[i][j] == MoveEnum.FROM_LOWER:
            backtrack = backtrack_lower
        elif backtrack[i][j] == MoveEnum.FROM_UPPER:
            backtrack = backtrack_upper
        elif backtrack[i][j] == MoveEnum.STOP:
            break
        else:
            raise ValueError("Invalid backtrack matrix.")
    return "".join(reversed(v_align)), "".join(reversed(w_align))


def global_alignment_gap(
    v: str, w: str, reward: int, mismatch: int, gap_open: int, gap_ext: int
) -> tuple[int, str, str]:
    """
    Returns the max score and the global alignment of v and w with affine
    gap penalties.
    """
    n, m = len(v) + 1, len(w) + 1
    lower = [[0] * m for _ in range(n)]
    upper = [[0] * m for _ in range(n)]
    middle = [[0] * m for _ in range(n)]
    backtrack_lower = [[MoveEnum.STOP] * m for _ in range(n)]
    backtrack_upper = [[MoveEnum.STOP] * m for _ in range(n)]
    backtrack_middle = [[MoveEnum.STOP] * m for _ in range(n)]

    for i in range(1, n):
        lower[i][0] = -(gap_open + gap_ext * (i - 1))
        upper[i][0] = INT_NEG_INFINITY
        middle[i][0] = lower[i][0]
        backtrack_lower[i][0] = MoveEnum.DOWN
        backtrack_middle[i][0] = MoveEnum.FROM_LOWER
    for j in range(1, m):
        lower[0][j] = INT_NEG_INFINITY
        upper[0][j] = -(gap_open + gap_ext * (j - 1))
        middle[0][j] = upper[0][j]
        backtrack_upper[0][j] = MoveEnum.RIGHT
        backtrack_middle[0][j] = MoveEnum.FROM_UPPER

    backtrack_lower[1][0] = MoveEnum.TO_LOWER
    backtrack_middle[1][0] = MoveEnum.DOWN

    backtrack_upper[0][1] = MoveEnum.TO_UPPER
    backtrack_middle[0][1] = MoveEnum.RIGHT

    for i in range(1, n):
        for j in range(1, m):
            lower[i][j], backtrack_lower[i][j] = max(
                (middle[i - 1][j] - gap_open, MoveEnum.TO_LOWER),
                (lower[i - 1][j] - gap_ext, MoveEnum.DOWN),
                key=lambda x: x[0],
            )
            upper[i][j], backtrack_upper[i][j] = max(
                (middle[i][j - 1] - gap_open, MoveEnum.TO_UPPER),
                (upper[i][j - 1] - gap_ext, MoveEnum.RIGHT),
                key=lambda x: x[0],
            )
            match = reward if v[i - 1] == w[j - 1] else -mismatch
            middle[i][j], backtrack_middle[i][j] = max(
                (lower[i][j], MoveEnum.FROM_LOWER),
                (upper[i][j], MoveEnum.FROM_UPPER),
                (middle[i - 1][j - 1] + match, MoveEnum.DOWN_RIGHT),
                key=lambda x: x[0],
            )

    max_score, backtrack = max(
        (lower[-1][-1], backtrack_lower),
        (upper[-1][-1], backtrack_upper),
        (middle[-1][-1], backtrack_middle),
        key=lambda x: x[0],
    )

    v_align, w_align = output_alignment_gap(
        backtrack,
        backtrack_lower,
        backtrack_upper,
        backtrack_middle,
        v,
        w,
        len(v),
        len(w),
    )
    return max_score, v_align, w_align


def find_middle_edge(
    w: str,
    v: str,
    top: int,
    bottom: int,
    left: int,
    right: int,
    reward: int,
    mismatch: int,
    in_del: int,
) -> tuple[tuple[int, int], tuple[int, int]]:
    """Returns a start and end node of the middle edge in alignment graph."""
    n, m = bottom - top, right - left
    max_j = (left + right) // 2
    source = [deque([0, 0], 2) for _ in range(n + 1)]
    sink = [deque([0, 0], 2) for _ in range(n + 1)]

    for i in range(n + 1):
        source[i].append(-in_del * i)
        sink[i].appendleft(-in_del * (n - i))

    for j in range(1 + left, max_j + 2):
        source[0].append(-in_del * (j - left))

        for i in range(1 + top, bottom + 1):
            match = reward if v[i - 1] == w[j - 1] else -mismatch
            score = max(
                source[i - top - 1][-1] - in_del,
                source[i - top][-1] - in_del,
                source[i - top - 1][0] + match,
            )
            source[i - top].append(score)
    for j in range(right - 1, max_j - 1, -1):
        sink[-1].appendleft(-in_del * (right - j))
        for i in range(bottom - 1, top - 1, -1):
            match = reward if v[i] == w[j] else -mismatch
            score = max(
                sink[i - top + 1][0] - in_del,
                sink[i - top][0] - in_del,
                sink[i - top + 1][-1] + match,
            )
            sink[i - top].appendleft(score)

    length = [source[i][0] + sink[i][0] for i in range(n + 1)]
    max_idx = length.index(max(length))
    max_i = top + max_idx
    if max_idx == n:
        max_next_i = max_i
        max_next_j = max_j + 1
    else:
        match = reward if v[max_i] == w[max_j] else -mismatch
        if sink[max_idx][0] == sink[max_idx][-1] - in_del:
            max_next_i, max_next_j = max_i, max_j + 1
        elif sink[max_idx][0] == sink[max_idx + 1][0] - in_del:
            max_next_i, max_next_j = max_i + 1, max_j
        elif sink[max_idx][0] == sink[max_idx + 1][-1] + match:
            max_next_i, max_next_j = max_i + 1, max_j + 1
        else:
            raise ValueError("Failed to find middle edge.")
    return (max_i, max_j), (max_next_i, max_next_j)


def backtrack_linear_space(
    w: str,
    v: str,
    top: int,
    bottom: int,
    left: int,
    right: int,
    reward: int,
    mismatch: int,
    in_del: int,
) -> list[MoveEnum]:
    """Returns the moves of the alignment of v and w in linear space."""
    if left == right:
        return [MoveEnum.DOWN for _ in range(bottom - top)]
    if bottom == top:
        return [MoveEnum.RIGHT for _ in range(right - left)]
    (mid_i, mid_j), (nxt_i, nxt_j) = find_middle_edge(
        w, v, top, bottom, left, right, reward, mismatch, in_del
    )
    moves1 = backtrack_linear_space(
        w, v, top, mid_i, left, mid_j, reward, mismatch, in_del
    )
    if mid_i + 1 == nxt_i and mid_j == nxt_j:
        moves2 = [MoveEnum.DOWN]
    elif mid_i == nxt_i and mid_j + 1 == nxt_j:
        moves2 = [MoveEnum.RIGHT]
    elif mid_i + 1 == nxt_i and mid_j + 1 == nxt_j:
        moves2 = [MoveEnum.DOWN_RIGHT]
    else:
        raise IndexError(f"Invalid Edge {(mid_i, mid_j), (nxt_i, nxt_j)}")
    moves3 = backtrack_linear_space(
        w, v, nxt_i, bottom, nxt_j, right, reward, mismatch, in_del
    )
    return moves1 + moves2 + moves3


def output_alignment_linear_space(
    backtrack: list[MoveEnum],
    w: str,
    v: str,
    reward: int,
    mismatch: int,
    in_del: int,
) -> tuple[int, str, str]:
    """
    Returns the alignment of v and w using the backtracking list.
    """
    v_align = []
    w_align = []
    score = 0
    i, j = len(v), len(w)
    for move in reversed(backtrack):
        if move == MoveEnum.DOWN:
            i -= 1
            v_align.append(v[i])
            w_align.append("-")
            score -= in_del
        elif move == MoveEnum.RIGHT:
            j -= 1
            v_align.append("-")
            w_align.append(w[j])
            score -= in_del
        elif move == MoveEnum.DOWN_RIGHT:
            i -= 1
            j -= 1
            v_align.append(v[i])
            w_align.append(w[j])
            score += reward if v[i] == w[j] else -mismatch
        elif move == MoveEnum.STOP:
            break
        else:
            raise ValueError("Invalid backtrack matrix.")
    return score, "".join(reversed(w_align)), "".join(reversed(v_align))


def global_alignment_linear_space(
    v: str, w: str, reward: int, mismatch: int, in_del: int
) -> tuple[int, str, str]:
    """Returns the global alignment of v and w in linear space."""
    backtrack = backtrack_linear_space(
        v, w, 0, len(w), 0, len(v), reward, mismatch, in_del
    )
    return output_alignment_linear_space(
        backtrack, v, w, reward, mismatch, in_del
    )


def output_alignment_3d(
    backtrack: list[list[list[MoveEnum]]],
    u: str,
    v: str,
    w: str,
    i: int,
    j: int,
    k: int,
) -> tuple[str, str, str]:
    """Returns the alignment of 3 strings u, v, and w."""
    u_align = []
    v_align = []
    w_align = []
    while i > 0 or j > 0 or k > 0:
        if backtrack[i][j][k] == MoveEnum.DOWN:
            i -= 1
            u_align.append(u[i])
            v_align.append("-")
            w_align.append("-")
        elif backtrack[i][j][k] == MoveEnum.RIGHT:
            j -= 1
            u_align.append("-")
            v_align.append(v[j])
            w_align.append("-")
        elif backtrack[i][j][k] == MoveEnum.FORWARD:
            k -= 1
            u_align.append("-")
            v_align.append("-")
            w_align.append(w[k])
        elif backtrack[i][j][k] == MoveEnum.DOWN_RIGHT:
            i -= 1
            j -= 1
            u_align.append(u[i])
            v_align.append(v[j])
            w_align.append("-")
        elif backtrack[i][j][k] == MoveEnum.DOWN_FORWARD:
            i -= 1
            k -= 1
            u_align.append(u[i])
            v_align.append("-")
            w_align.append(w[k])
        elif backtrack[i][j][k] == MoveEnum.RIGHT_FORWARD:
            j -= 1
            k -= 1
            u_align.append("-")
            v_align.append(v[j])
            w_align.append(w[k])
        elif backtrack[i][j][k] == MoveEnum.DIAGONAL:
            i -= 1
            j -= 1
            k -= 1
            u_align.append(u[i])
            v_align.append(v[j])
            w_align.append(w[k])
        elif backtrack[i][j][k] == MoveEnum.STOP:
            break
        else:
            raise ValueError("Invalid backtrack matrix.")
    return (
        "".join(reversed(u_align)),
        "".join(reversed(v_align)),
        "".join(reversed(w_align)),
    )


def global_alignment_3_dim(
    u: str, v: str, w: str
) -> tuple[int, str, str, str]:
    """Returns the longest common subsequence of 3 strings."""
    l, n, m = len(u) + 1, len(v) + 1, len(w) + 1
    score = [[[0] * m for _ in range(n)] for _ in range(l)]
    backtrack = [[[MoveEnum.STOP] * m for _ in range(n)] for _ in range(l)]
    for i in range(1, l):
        backtrack[i][0][0] = MoveEnum.DOWN
    for j in range(1, n):
        backtrack[0][j][0] = MoveEnum.RIGHT
    for k in range(1, m):
        backtrack[0][0][k] = MoveEnum.FORWARD
    for i in range(1, l):
        for j in range(1, n):
            backtrack[i][j][0] = MoveEnum.DOWN_RIGHT
        for k in range(1, m):
            backtrack[i][0][k] = MoveEnum.DOWN_FORWARD
    for j in range(1, n):
        for k in range(1, m):
            backtrack[0][j][k] = MoveEnum.RIGHT_FORWARD

    for i in range(1, l):
        for j in range(1, n):
            for k in range(1, m):
                match = 1 if u[i - 1] == v[j - 1] == w[k - 1] else 0
                paths = [
                    (score[i - 1][j][k], MoveEnum.DOWN),
                    (score[i][j - 1][k], MoveEnum.RIGHT),
                    (score[i][j][k - 1], MoveEnum.FORWARD),
                    (score[i - 1][j - 1][k], MoveEnum.DOWN_RIGHT),
                    (score[i - 1][j][k - 1], MoveEnum.DOWN_FORWARD),
                    (score[i][j - 1][k - 1], MoveEnum.RIGHT_FORWARD),
                    (score[i - 1][j - 1][k - 1] + match, MoveEnum.DIAGONAL),
                ]
                score[i][j][k], backtrack[i][j][k] = max(
                    paths, key=lambda x: x[0]
                )

    u_align, v_align, w_align = output_alignment_3d(
        backtrack, u, v, w, len(u), len(v), len(w)
    )
    return score[-1][-1][-1], u_align, v_align, w_align
