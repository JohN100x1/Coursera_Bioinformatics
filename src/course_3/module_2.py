from itertools import accumulate

from course_3.module_1 import MoveEnum

PAM250 = {
    "A": {
        "A": 2,
        "C": -2,
        "E": 0,
        "D": 0,
        "G": 1,
        "F": -3,
        "I": -1,
        "H": -1,
        "K": -1,
        "M": -1,
        "L": -2,
        "N": 0,
        "Q": 0,
        "P": 1,
        "S": 1,
        "R": -2,
        "T": 1,
        "W": -6,
        "V": 0,
        "Y": -3,
    },
    "C": {
        "A": -2,
        "C": 12,
        "E": -5,
        "D": -5,
        "G": -3,
        "F": -4,
        "I": -2,
        "H": -3,
        "K": -5,
        "M": -5,
        "L": -6,
        "N": -4,
        "Q": -5,
        "P": -3,
        "S": 0,
        "R": -4,
        "T": -2,
        "W": -8,
        "V": -2,
        "Y": 0,
    },
    "E": {
        "A": 0,
        "C": -5,
        "E": 4,
        "D": 3,
        "G": 0,
        "F": -5,
        "I": -2,
        "H": 1,
        "K": 0,
        "M": -2,
        "L": -3,
        "N": 1,
        "Q": 2,
        "P": -1,
        "S": 0,
        "R": -1,
        "T": 0,
        "W": -7,
        "V": -2,
        "Y": -4,
    },
    "D": {
        "A": 0,
        "C": -5,
        "E": 3,
        "D": 4,
        "G": 1,
        "F": -6,
        "I": -2,
        "H": 1,
        "K": 0,
        "M": -3,
        "L": -4,
        "N": 2,
        "Q": 2,
        "P": -1,
        "S": 0,
        "R": -1,
        "T": 0,
        "W": -7,
        "V": -2,
        "Y": -4,
    },
    "G": {
        "A": 1,
        "C": -3,
        "E": 0,
        "D": 1,
        "G": 5,
        "F": -5,
        "I": -3,
        "H": -2,
        "K": -2,
        "M": -3,
        "L": -4,
        "N": 0,
        "Q": -1,
        "P": 0,
        "S": 1,
        "R": -3,
        "T": 0,
        "W": -7,
        "V": -1,
        "Y": -5,
    },
    "F": {
        "A": -3,
        "C": -4,
        "E": -5,
        "D": -6,
        "G": -5,
        "F": 9,
        "I": 1,
        "H": -2,
        "K": -5,
        "M": 0,
        "L": 2,
        "N": -3,
        "Q": -5,
        "P": -5,
        "S": -3,
        "R": -4,
        "T": -3,
        "W": 0,
        "V": -1,
        "Y": 7,
    },
    "I": {
        "A": -1,
        "C": -2,
        "E": -2,
        "D": -2,
        "G": -3,
        "F": 1,
        "I": 5,
        "H": -2,
        "K": -2,
        "M": 2,
        "L": 2,
        "N": -2,
        "Q": -2,
        "P": -2,
        "S": -1,
        "R": -2,
        "T": 0,
        "W": -5,
        "V": 4,
        "Y": -1,
    },
    "H": {
        "A": -1,
        "C": -3,
        "E": 1,
        "D": 1,
        "G": -2,
        "F": -2,
        "I": -2,
        "H": 6,
        "K": 0,
        "M": -2,
        "L": -2,
        "N": 2,
        "Q": 3,
        "P": 0,
        "S": -1,
        "R": 2,
        "T": -1,
        "W": -3,
        "V": -2,
        "Y": 0,
    },
    "K": {
        "A": -1,
        "C": -5,
        "E": 0,
        "D": 0,
        "G": -2,
        "F": -5,
        "I": -2,
        "H": 0,
        "K": 5,
        "M": 0,
        "L": -3,
        "N": 1,
        "Q": 1,
        "P": -1,
        "S": 0,
        "R": 3,
        "T": 0,
        "W": -3,
        "V": -2,
        "Y": -4,
    },
    "M": {
        "A": -1,
        "C": -5,
        "E": -2,
        "D": -3,
        "G": -3,
        "F": 0,
        "I": 2,
        "H": -2,
        "K": 0,
        "M": 6,
        "L": 4,
        "N": -2,
        "Q": -1,
        "P": -2,
        "S": -2,
        "R": 0,
        "T": -1,
        "W": -4,
        "V": 2,
        "Y": -2,
    },
    "L": {
        "A": -2,
        "C": -6,
        "E": -3,
        "D": -4,
        "G": -4,
        "F": 2,
        "I": 2,
        "H": -2,
        "K": -3,
        "M": 4,
        "L": 6,
        "N": -3,
        "Q": -2,
        "P": -3,
        "S": -3,
        "R": -3,
        "T": -2,
        "W": -2,
        "V": 2,
        "Y": -1,
    },
    "N": {
        "A": 0,
        "C": -4,
        "E": 1,
        "D": 2,
        "G": 0,
        "F": -3,
        "I": -2,
        "H": 2,
        "K": 1,
        "M": -2,
        "L": -3,
        "N": 2,
        "Q": 1,
        "P": 0,
        "S": 1,
        "R": 0,
        "T": 0,
        "W": -4,
        "V": -2,
        "Y": -2,
    },
    "Q": {
        "A": 0,
        "C": -5,
        "E": 2,
        "D": 2,
        "G": -1,
        "F": -5,
        "I": -2,
        "H": 3,
        "K": 1,
        "M": -1,
        "L": -2,
        "N": 1,
        "Q": 4,
        "P": 0,
        "S": -1,
        "R": 1,
        "T": -1,
        "W": -5,
        "V": -2,
        "Y": -4,
    },
    "P": {
        "A": 1,
        "C": -3,
        "E": -1,
        "D": -1,
        "G": 0,
        "F": -5,
        "I": -2,
        "H": 0,
        "K": -1,
        "M": -2,
        "L": -3,
        "N": 0,
        "Q": 0,
        "P": 6,
        "S": 1,
        "R": 0,
        "T": 0,
        "W": -6,
        "V": -1,
        "Y": -5,
    },
    "S": {
        "A": 1,
        "C": 0,
        "E": 0,
        "D": 0,
        "G": 1,
        "F": -3,
        "I": -1,
        "H": -1,
        "K": 0,
        "M": -2,
        "L": -3,
        "N": 1,
        "Q": -1,
        "P": 1,
        "S": 2,
        "R": 0,
        "T": 1,
        "W": -2,
        "V": -1,
        "Y": -3,
    },
    "R": {
        "A": -2,
        "C": -4,
        "E": -1,
        "D": -1,
        "G": -3,
        "F": -4,
        "I": -2,
        "H": 2,
        "K": 3,
        "M": 0,
        "L": -3,
        "N": 0,
        "Q": 1,
        "P": 0,
        "S": 0,
        "R": 6,
        "T": -1,
        "W": 2,
        "V": -2,
        "Y": -4,
    },
    "T": {
        "A": 1,
        "C": -2,
        "E": 0,
        "D": 0,
        "G": 0,
        "F": -3,
        "I": 0,
        "H": -1,
        "K": 0,
        "M": -1,
        "L": -2,
        "N": 0,
        "Q": -1,
        "P": 0,
        "S": 1,
        "R": -1,
        "T": 3,
        "W": -5,
        "V": 0,
        "Y": -3,
    },
    "W": {
        "A": -6,
        "C": -8,
        "E": -7,
        "D": -7,
        "G": -7,
        "F": 0,
        "I": -5,
        "H": -3,
        "K": -3,
        "M": -4,
        "L": -2,
        "N": -4,
        "Q": -5,
        "P": -6,
        "S": -2,
        "R": 2,
        "T": -5,
        "W": 17,
        "V": -6,
        "Y": 0,
    },
    "V": {
        "A": 0,
        "C": -2,
        "E": -2,
        "D": -2,
        "G": -1,
        "F": -1,
        "I": 4,
        "H": -2,
        "K": -2,
        "M": 2,
        "L": 2,
        "N": -2,
        "Q": -2,
        "P": -1,
        "S": -1,
        "R": -2,
        "T": 0,
        "W": -6,
        "V": 4,
        "Y": -2,
    },
    "Y": {
        "A": -3,
        "C": 0,
        "E": -4,
        "D": -4,
        "G": -5,
        "F": 7,
        "I": -1,
        "H": 0,
        "K": -4,
        "M": -2,
        "L": -1,
        "N": -2,
        "Q": -4,
        "P": -5,
        "S": -3,
        "R": -4,
        "T": -3,
        "W": 0,
        "V": -2,
        "Y": 10,
    },
}
BLOSUM62 = {
    "A": {
        "A": 4,
        "C": 0,
        "D": -2,
        "E": -1,
        "F": -2,
        "G": 0,
        "H": -2,
        "I": -1,
        "K": -1,
        "L": -1,
        "M": -1,
        "N": -2,
        "P": -1,
        "Q": -1,
        "R": -1,
        "S": 1,
        "T": 0,
        "V": 0,
        "W": -3,
        "Y": -2,
    },
    "C": {
        "A": 0,
        "C": 9,
        "D": -3,
        "E": -4,
        "F": -2,
        "G": -3,
        "H": -3,
        "I": -1,
        "K": -3,
        "L": -1,
        "M": -1,
        "N": -3,
        "P": -3,
        "Q": -3,
        "R": -3,
        "S": -1,
        "T": -1,
        "V": -1,
        "W": -2,
        "Y": -2,
    },
    "D": {
        "A": -2,
        "C": -3,
        "D": 6,
        "E": 2,
        "F": -3,
        "G": -1,
        "H": -1,
        "I": -3,
        "K": -1,
        "L": -4,
        "M": -3,
        "N": 1,
        "P": -1,
        "Q": 0,
        "R": -2,
        "S": 0,
        "T": -1,
        "V": -3,
        "W": -4,
        "Y": -3,
    },
    "E": {
        "A": -1,
        "C": -4,
        "D": 2,
        "E": 5,
        "F": -3,
        "G": -2,
        "H": 0,
        "I": -3,
        "K": 1,
        "L": -3,
        "M": -2,
        "N": 0,
        "P": -1,
        "Q": 2,
        "R": 0,
        "S": 0,
        "T": -1,
        "V": -2,
        "W": -3,
        "Y": -2,
    },
    "F": {
        "A": -2,
        "C": -2,
        "D": -3,
        "E": -3,
        "F": 6,
        "G": -3,
        "H": -1,
        "I": 0,
        "K": -3,
        "L": 0,
        "M": 0,
        "N": -3,
        "P": -4,
        "Q": -3,
        "R": -3,
        "S": -2,
        "T": -2,
        "V": -1,
        "W": 1,
        "Y": 3,
    },
    "G": {
        "A": 0,
        "C": -3,
        "D": -1,
        "E": -2,
        "F": -3,
        "G": 6,
        "H": -2,
        "I": -4,
        "K": -2,
        "L": -4,
        "M": -3,
        "N": 0,
        "P": -2,
        "Q": -2,
        "R": -2,
        "S": 0,
        "T": -2,
        "V": -3,
        "W": -2,
        "Y": -3,
    },
    "H": {
        "A": -2,
        "C": -3,
        "D": -1,
        "E": 0,
        "F": -1,
        "G": -2,
        "H": 8,
        "I": -3,
        "K": -1,
        "L": -3,
        "M": -2,
        "N": 1,
        "P": -2,
        "Q": 0,
        "R": 0,
        "S": -1,
        "T": -2,
        "V": -3,
        "W": -2,
        "Y": 2,
    },
    "I": {
        "A": -1,
        "C": -1,
        "D": -3,
        "E": -3,
        "F": 0,
        "G": -4,
        "H": -3,
        "I": 4,
        "K": -3,
        "L": 2,
        "M": 1,
        "N": -3,
        "P": -3,
        "Q": -3,
        "R": -3,
        "S": -2,
        "T": -1,
        "V": 3,
        "W": -3,
        "Y": -1,
    },
    "K": {
        "A": -1,
        "C": -3,
        "D": -1,
        "E": 1,
        "F": -3,
        "G": -2,
        "H": -1,
        "I": -3,
        "K": 5,
        "L": -2,
        "M": -1,
        "N": 0,
        "P": -1,
        "Q": 1,
        "R": 2,
        "S": 0,
        "T": -1,
        "V": -2,
        "W": -3,
        "Y": -2,
    },
    "L": {
        "A": -1,
        "C": -1,
        "D": -4,
        "E": -3,
        "F": 0,
        "G": -4,
        "H": -3,
        "I": 2,
        "K": -2,
        "L": 4,
        "M": 2,
        "N": -3,
        "P": -3,
        "Q": -2,
        "R": -2,
        "S": -2,
        "T": -1,
        "V": 1,
        "W": -2,
        "Y": -1,
    },
    "M": {
        "A": -1,
        "C": -1,
        "D": -3,
        "E": -2,
        "F": 0,
        "G": -3,
        "H": -2,
        "I": 1,
        "K": -1,
        "L": 2,
        "M": 5,
        "N": -2,
        "P": -2,
        "Q": 0,
        "R": -1,
        "S": -1,
        "T": -1,
        "V": 1,
        "W": -1,
        "Y": -1,
    },
    "N": {
        "A": -2,
        "C": -3,
        "D": 1,
        "E": 0,
        "F": -3,
        "G": 0,
        "H": 1,
        "I": -3,
        "K": 0,
        "L": -3,
        "M": -2,
        "N": 6,
        "P": -2,
        "Q": 0,
        "R": 0,
        "S": 1,
        "T": 0,
        "V": -3,
        "W": -4,
        "Y": -2,
    },
    "P": {
        "A": -1,
        "C": -3,
        "D": -1,
        "E": -1,
        "F": -4,
        "G": -2,
        "H": -2,
        "I": -3,
        "K": -1,
        "L": -3,
        "M": -2,
        "N": -2,
        "P": 7,
        "Q": -1,
        "R": -2,
        "S": -1,
        "T": -1,
        "V": -2,
        "W": -4,
        "Y": -3,
    },
    "Q": {
        "A": -1,
        "C": -3,
        "D": 0,
        "E": 2,
        "F": -3,
        "G": -2,
        "H": 0,
        "I": -3,
        "K": 1,
        "L": -2,
        "M": 0,
        "N": 0,
        "P": -1,
        "Q": 5,
        "R": 1,
        "S": 0,
        "T": -1,
        "V": -2,
        "W": -2,
        "Y": -1,
    },
    "R": {
        "A": -1,
        "C": -3,
        "D": -2,
        "E": 0,
        "F": -3,
        "G": -2,
        "H": 0,
        "I": -3,
        "K": 2,
        "L": -2,
        "M": -1,
        "N": 0,
        "P": -2,
        "Q": 1,
        "R": 5,
        "S": -1,
        "T": -1,
        "V": -3,
        "W": -3,
        "Y": -2,
    },
    "S": {
        "A": 1,
        "C": -1,
        "D": 0,
        "E": 0,
        "F": -2,
        "G": 0,
        "H": -1,
        "I": -2,
        "K": 0,
        "L": -2,
        "M": -1,
        "N": 1,
        "P": -1,
        "Q": 0,
        "R": -1,
        "S": 4,
        "T": 1,
        "V": -2,
        "W": -3,
        "Y": -2,
    },
    "T": {
        "A": 0,
        "C": -1,
        "D": -1,
        "E": -1,
        "F": -2,
        "G": -2,
        "H": -2,
        "I": -1,
        "K": -1,
        "L": -1,
        "M": -1,
        "N": 0,
        "P": -1,
        "Q": -1,
        "R": -1,
        "S": 1,
        "T": 5,
        "V": 0,
        "W": -2,
        "Y": -2,
    },
    "V": {
        "A": 0,
        "C": -1,
        "D": -3,
        "E": -2,
        "F": -1,
        "G": -3,
        "H": -3,
        "I": 3,
        "K": -2,
        "L": 1,
        "M": 1,
        "N": -3,
        "P": -2,
        "Q": -2,
        "R": -3,
        "S": -2,
        "T": 0,
        "V": 4,
        "W": -3,
        "Y": -1,
    },
    "W": {
        "A": -3,
        "C": -2,
        "D": -4,
        "E": -3,
        "F": 1,
        "G": -2,
        "H": -2,
        "I": -3,
        "K": -3,
        "L": -2,
        "M": -1,
        "N": -4,
        "P": -4,
        "Q": -2,
        "R": -3,
        "S": -3,
        "T": -2,
        "V": -3,
        "W": 11,
        "Y": 2,
    },
    "Y": {
        "A": -2,
        "C": -2,
        "D": -3,
        "E": -2,
        "F": 3,
        "G": -3,
        "H": 2,
        "I": -1,
        "K": -2,
        "L": -1,
        "M": -1,
        "N": -2,
        "P": -3,
        "Q": -1,
        "R": -2,
        "S": -2,
        "T": -2,
        "V": -1,
        "W": 2,
        "Y": 7,
    },
}


def output_alignment(
    backtrack: list[list[MoveEnum]], v: str, w: str, i: int, j: int
) -> tuple[str, str]:
    """
    Returns the alignment of v and w using the backtracking matrix and
    (i, j)-start.
    """
    v_align = []
    w_align = []
    while i > 0 or j > 0:
        if backtrack[i][j] == MoveEnum.DOWN:
            i -= 1
            v_align.append(v[i])
            w_align.append("-")
        elif backtrack[i][j] == MoveEnum.RIGHT:
            j -= 1
            v_align.append("-")
            w_align.append(w[j])
        elif backtrack[i][j] == MoveEnum.DOWN_RIGHT:
            i -= 1
            j -= 1
            v_align.append(v[i])
            w_align.append(w[j])
        elif backtrack[i][j] == MoveEnum.STOP:
            break
        else:
            raise ValueError("Invalid backtrack matrix.")
    return "".join(reversed(v_align)), "".join(reversed(w_align))


def global_alignment(
    v: str, w: str, reward: int, mismatch: int, in_del: int
) -> tuple[int, str, str]:
    """
    Returns the max score and the global alignment of v and w.
    Hint: Top left -> Bottom right
    """
    n, m = len(v) + 1, len(w) + 1
    score = [[0] * m for _ in range(n)]
    backtrack = [[MoveEnum.STOP] * m for _ in range(n)]
    for i in range(1, n):
        score[i][0] = score[i - 1][0] - in_del
        backtrack[i][0] = MoveEnum.DOWN
    score[0][1:m] = list(accumulate(-in_del for _ in range(m - 1)))
    backtrack[0][1:m] = [MoveEnum.RIGHT for _ in range(m - 1)]

    for i in range(1, n):
        for j in range(1, m):
            match = reward if v[i - 1] == w[j - 1] else -mismatch
            # Important: Re-ordering this will return other solutions
            paths = [
                (score[i - 1][j] - in_del, MoveEnum.DOWN),
                (score[i][j - 1] - in_del, MoveEnum.RIGHT),
                (score[i - 1][j - 1] + match, MoveEnum.DOWN_RIGHT),
            ]
            score[i][j], backtrack[i][j] = max(paths, key=lambda x: x[0])

    v_align, w_align = output_alignment(backtrack, v, w, len(v), len(w))
    return score[-1][-1], v_align, w_align


def local_alignment(
    v: str,
    w: str,
    reward: int | None = None,
    mismatch: int | None = None,
    in_del: int = 5,
) -> tuple[int, str, str]:
    """
    Returns the max score and the local alignment of protein v and w.
    Default scoring matrix is PAM250.
    Hint: Any Col Row -> Any Col Row
    """
    if reward is None or mismatch is None:

        def scoring(x: str, y: str) -> int:
            return PAM250[x][y]

    else:

        def scoring(x: str, y: str) -> int:
            return reward if x == y else -mismatch

    n, m = len(v) + 1, len(w) + 1
    score = [[0] * m for _ in range(n)]
    backtrack = [[MoveEnum.STOP] * m for _ in range(n)]

    max_score = 0
    max_i, max_j = 0, 0
    for i in range(1, n):
        for j in range(1, m):
            match = scoring(v[i - 1], w[j - 1])
            # Important: Re-ordering this will return other solutions
            paths = [
                (0, MoveEnum.STOP),
                (score[i - 1][j] - in_del, MoveEnum.DOWN),
                (score[i][j - 1] - in_del, MoveEnum.RIGHT),
                (score[i - 1][j - 1] + match, MoveEnum.DOWN_RIGHT),
            ]
            score[i][j], backtrack[i][j] = max(paths, key=lambda x: x[0])
            if score[i][j] > max_score:
                max_score = score[i][j]
                max_i, max_j = i, j

    v_align, w_align = output_alignment(backtrack, v, w, max_i, max_j)
    return max_score, v_align, w_align


def edit_distance(v: str, w: str) -> int:
    """Returns the edit distance between two strings v and w."""
    n, m = len(v) + 1, len(w) + 1
    dist = [[0] * m for _ in range(n)]
    for i in range(1, n):
        dist[i][0] = i
    for j in range(1, m):
        dist[0][j] = j
    for i in range(1, n):
        for j in range(1, m):
            dist_hor = dist[i][j - 1] + 1
            dist_ver = dist[i - 1][j] + 1
            if v[i - 1] == w[j - 1]:
                dist_diag = dist[i - 1][j - 1]
            else:
                dist_diag = dist[i - 1][j - 1] + 1
            dist[i][j] = min(dist_hor, dist_ver, dist_diag)
    return dist[-1][-1]


def fitting_alignment(
    v: str,
    w: str,
    reward: int | None = None,
    mismatch: int | None = None,
    in_del: int = 1,
) -> tuple[int, str, str]:
    """
    Returns the score and the fitting alignment of protein v and w.
    Default scoring matrix is BLOSUM62.
    Hint: 1st Col -> Last Col
    """
    if reward is None or mismatch is None:

        def scoring(x: str, y: str) -> int:
            return BLOSUM62[x][y]

    else:

        def scoring(x: str, y: str) -> int:
            return reward if x == y else -mismatch

    n, m = len(v) + 1, len(w) + 1
    score = [[0] * m for _ in range(n)]
    backtrack = [[MoveEnum.STOP] * m for _ in range(n)]
    score[0][1:m] = list(accumulate(-in_del for _ in range(m - 1)))
    backtrack[0][1:m] = [MoveEnum.RIGHT for _ in range(m - 1)]

    for i in range(1, n):
        for j in range(1, m):
            match = scoring(v[i - 1], w[j - 1])
            # Important: Re-ordering this will return other solutions
            paths = [
                (score[i - 1][j] - in_del, MoveEnum.DOWN),
                (score[i][j - 1] - in_del, MoveEnum.RIGHT),
                (score[i - 1][j - 1] + match, MoveEnum.DOWN_RIGHT),
            ]
            score[i][j], backtrack[i][j] = max(paths, key=lambda x: x[0])

    max_score, max_i = max((score[i][-1], i) for i in range(n))
    v_align, w_align = output_alignment(backtrack, v, w, max_i, len(w))
    return max_score, v_align, w_align


def overlap_alignment(
    v: str, w: str, reward: int, mismatch: int, in_del: int
) -> tuple[int, str, str]:
    """
    Returns the score and the overlap alignment of v and w.
    Hint: 1st Col -> Bottom Row
    """
    n, m = len(v) + 1, len(w) + 1
    score = [[0] * m for _ in range(n)]
    backtrack = [[MoveEnum.STOP] * m for _ in range(n)]
    score[0][1:m] = list(accumulate(-in_del for _ in range(m - 1)))
    backtrack[0][1:m] = [MoveEnum.RIGHT for _ in range(m - 1)]

    for i in range(1, n):
        for j in range(1, m):
            match = reward if v[i - 1] == w[j - 1] else -mismatch
            # Important: Re-ordering this will return other solutions
            paths = [
                (score[i - 1][j - 1] + match, MoveEnum.DOWN_RIGHT),
                (score[i][j - 1] - in_del, MoveEnum.RIGHT),
                (score[i - 1][j] - in_del, MoveEnum.DOWN),
            ]
            score[i][j], backtrack[i][j] = max(paths, key=lambda x: x[0])

    max_score, max_j = max((score[-1][j], j) for j in range(m))
    v_align, w_align = output_alignment(backtrack, v, w, len(v), max_j)
    return max_score, v_align, w_align
