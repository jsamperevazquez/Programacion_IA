import pytest
from ejer50 import hamming_distance


def test_hamming_distance():
    assert 0 == hamming_distance('ACTG', 'ACTG')
    assert 2 == hamming_distance('ACTG', 'ACGT')


def test_value_exception():
    with pytest.raises(ValueError):
        hamming_distance('ACGT', 'AC')


def test_type_exception():
    with pytest.raises(TypeError):
        hamming_distance(1234)