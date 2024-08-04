import pytest

from course_3.module_1 import (
    longest_common_subseq,
    longest_path_dag,
    manhattan_tourist,
    min_num_coins,
)


@pytest.mark.parametrize(
    "target, coins, min_coins",
    [
        (40, [50, 25, 20, 10, 5, 1], 2),
        (7, [1, 5], 3),
        (10, [1, 2, 3, 4, 5, 10], 1),
        (10, [10, 5, 4, 3, 2, 1], 1),
        (11, [1, 5], 3),
        (12, [9, 6, 1], 2),
        (8074, [24, 13, 12, 7, 5, 3, 1], 338),
    ],
)
def test_min_coins(target: int, coins: list[int], min_coins: int) -> None:
    assert min_num_coins(target, coins) == min_coins


@pytest.mark.parametrize(
    "n, m, down, right, max_dist",
    [
        (
            4,
            4,
            [
                [1, 0, 2, 4, 3],
                [4, 6, 5, 2, 1],
                [4, 4, 5, 2, 1],
                [5, 6, 8, 5, 3],
            ],
            [
                [3, 2, 4, 0],
                [3, 2, 4, 2],
                [0, 7, 3, 3],
                [3, 3, 0, 2],
                [1, 3, 2, 2],
            ],
            34,
        ),
        (2, 2, [[20, 0, 0], [20, 0, 0]], [[0, 0], [0, 0], [10, 10]], 60),
        (2, 2, [[0, 0, 20], [0, 0, 20]], [[10, 10], [0, 0], [0, 0]], 60),
        (2, 2, [[20, 0, 0], [0, 0, 0]], [[0, 30], [0, 0], [0, 0]], 30),
        (
            5,
            3,
            [
                [20, 5, 0, 10],
                [0, 5, 10, 0],
                [10, 10, 0, 15],
                [0, 20, 20, 25],
                [30, 10, 5, 30],
            ],
            [
                [0, 30, 15],
                [10, 20, 10],
                [10, 10, 20],
                [20, 25, 30],
                [15, 35, 40],
                [15, 10, 25],
            ],
            175,
        ),
        (
            3,
            5,
            [
                [0, 5, 10, 0, 10, 10],
                [15, 0, 20, 20, 25, 30],
                [10, 5, 30, 15, 0, 20],
            ],
            [
                [0, 30, 15, 10, 20],
                [10, 10, 10, 20, 20],
                [25, 30, 15, 35, 40],
                [15, 10, 25, 15, 20],
            ],
            180,
        ),
    ],
)
def test_manhattan_tourist(
    n: int,
    m: int,
    down: list[list[int]],
    right: list[list[int]],
    max_dist: int,
) -> None:
    assert manhattan_tourist(n, m, down, right) == max_dist


@pytest.mark.parametrize(
    "v, w, sub_string",
    [
        ("AACCTTGG", "ACACTGTGA", "AACTTG"),
        ("GACT", "ATG", "AT"),
        ("ACTGAG", "GACTGG", "ACTGG"),
        ("AC", "AC", "AC"),
        ("GGGGT", "CCCCT", "T"),
        ("TCCCC", "TGGGG", "T"),
        ("AA", "CGTGGAT", "A"),
        ("GGTGACGT", "CT", "CT"),
    ],
)
def test_longest_common_subseq(v: str, w: str, sub_string: str) -> None:
    assert longest_common_subseq(v, w) == sub_string


@pytest.mark.parametrize(
    "dag, start, end, max_dist, max_path",
    [
        (
            {
                0: [(1, 7), (2, 4)],
                1: [(4, 1)],
                2: [(3, 2)],
                3: [(4, 3)],
                4: [],
            },
            0,
            4,
            9,
            [0, 2, 3, 4],
        ),
        (
            {0: [(1, 1), (3, 10)], 1: [(2, 1)], 2: [(3, 1)], 3: []},
            0,
            3,
            10,
            [0, 3],
        ),
        (
            {0: [(1, 2), (2, 1)], 1: [(3, 3)], 2: [(3, 3)], 3: []},
            0,
            3,
            5,
            [0, 1, 3],
        ),
        (
            {0: [(1, 1), (2, 5)], 1: [(3, 10)], 2: [(3, 1)], 3: []},
            0,
            3,
            11,
            [0, 1, 3],
        ),
        (
            {1: [(2, 1), (3, 5)], 2: [(4, 10)], 3: [(4, 1)], 4: []},
            1,
            4,
            11,
            [1, 2, 4],
        ),
        (
            {1: [(2, 1)], 2: [(3, 3)], 3: [(10, 1)], 10: []},
            1,
            10,
            5,
            [1, 2, 3, 10],
        ),
        ({0: [(4, 7)], 4: []}, 0, 4, 7, [0, 4]),
    ],
)
def test_longest_path_dag(
    dag: dict[int, list[tuple[int, int]]],
    start: int,
    end: int,
    max_dist: int,
    max_path: list[int],
) -> None:
    distance, path = longest_path_dag(dag, start, end)
    assert distance == max_dist
    assert path == max_path


def test_longest_path_dag_str() -> None:
    dag = {
        "a": [("b", 5), ("c", 6), ("d", 5)],
        "b": [("c", 2), ("f", 9)],
        "c": [("e", 4), ("f", 3), ("g", 7)],
        "d": [("e", 4), ("f", 5)],
        "e": [("g", 2)],
        "f": [("g", 1)],
    }
    distance, path = longest_path_dag(dag, "a", "g")
    assert distance == 15
    assert path == ["a", "b", "f", "g"]
