from bowling import get_total_score
import pytest

@pytest.mark.parametrize("input, expected_score", [
    ("X 45 4/ 32", 46),
    ("X 34", 24),
    ("23 54 00 10", 15),
    ("X X 32", 40),
    ("X 2/ 33", 39)
])
def test_get_total_score(input, expected_score):
    result = get_total_score(input)
    assert result == expected_score
