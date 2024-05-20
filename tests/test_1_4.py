from task_1_4_0_find_clumps import find_clumps


def test_find_clumps() -> None:
    text = (
        "CGGACTCGACAGATGTGAAGAACGACAATGTGAAGAC"
        "TCGACACGACAGAGTGAAGAGAAGAGGAAACATTGTAA"
    )
    patterns = find_clumps(text, 5, 50, 4)
    assert patterns == {"CGACA", "GAAGA"}
