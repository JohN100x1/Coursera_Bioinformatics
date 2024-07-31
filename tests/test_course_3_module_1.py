from course_3.module_1 import (
    min_num_coins,
    manhattan_tourist,
    longest_common_subseq,
    longest_path_dag,
)

# TODO: add all debug cases (small only)


def test_min_coins() -> None:
    assert min_num_coins(40, [50, 25, 20, 10, 5, 1]) == 2


def test_manhattan_tourist() -> None:
    assert (
        manhattan_tourist(
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
        )
        == 34
    )


def test_longest_common_subseq() -> None:
    assert longest_common_subseq("AACCTTGG", "ACACTGTGA") == "AACTTG"


def test_longest_path_dag() -> None:
    dag = {0: [(1, 7), (2, 4)], 2: [(3, 2)], 1: [(4, 1)], 3: [(4, 3)], 4: []}
    distance, path = longest_path_dag(dag, 0, 4)
    assert distance == 9
    assert path == [0, 2, 3, 4]


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
