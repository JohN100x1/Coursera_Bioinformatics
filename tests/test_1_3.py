from task_1_3_0_reverse_complement import reverse_complement
from task_1_3_1_pattern_matching import pattern_matching


def test_reverse_complement() -> None:
    complement = reverse_complement("AAAACCCGGT")
    assert complement == "ACCGGGTTTT"


def test_pattern_matching() -> None:
    indexes = pattern_matching("ATAT", "GATATATGCATATACTT")
    assert indexes == [1, 3, 9]
