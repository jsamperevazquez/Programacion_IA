import pytest
from ejer53 import User, InmutableUser


def test_create_inmutable():
    user1 = InmutableUser('Angel', 'Sampere', 'Ritrux', '<PASSWORD>',
                          key_number='4539 3195 0343 6467')
    assert user1.full_name == 'Angel Sampere'


def test_invalid_key_numbers():
    with pytest.raises(ValueError):
        user2 = InmutableUser('Angel', 'Sampere', 'Ritrux', '<PASSWORD>',
                              key_number='123456789')
