import pytest
from ejer48 import validate_number


def test_validate_number():
    assert validate_number('4539 3195 0343 6467')
    assert pytest.raises(ValueError, validate_number, '4 3195 0343 6467')
    assert pytest.raises(ValueError, validate_number, '8273 1232 7352 0569')

