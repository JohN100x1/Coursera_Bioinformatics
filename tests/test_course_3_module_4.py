from course_3.module_4 import greedy_sorting, count_breakpoints


def test_greedy_sorting() -> None:
    perm = [-3, +4, +1, +5, -2]
    output = [
        [-1, -4, +3, +5, -2],
        [+1, -4, +3, +5, -2],
        [+1, +2, -5, -3, +4],
        [+1, +2, +3, +5, +4],
        [+1, +2, +3, -4, -5],
        [+1, +2, +3, +4, -5],
        [+1, +2, +3, +4, +5],
    ]
    for actual, expected in zip(greedy_sorting(perm), output):
        assert actual == expected


def test_count_breakpoints() -> None:
    perm = [+3, +4, +5, -12, -8, -7, -6, +1, +2, +10, +9, -11, +13, +14]
    assert count_breakpoints(perm) == 8
