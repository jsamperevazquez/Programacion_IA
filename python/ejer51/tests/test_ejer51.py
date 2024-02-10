import pytest
from ejer51 import BlackJack


def test_min_age():
    with pytest.raises(ValueError):
        BlackJack("Menor", 14)

