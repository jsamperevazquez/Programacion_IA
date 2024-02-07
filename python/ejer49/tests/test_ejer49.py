import pytest
from ejer49 import Vehicle


def test_vehicle_init():
    vehicle1 = Vehicle(100, 3000)
    assert vehicle1.max_speed == 100
    assert vehicle1.kms == 3000


def test_vehicle_negative_speed():
    with pytest.raises(ValueError):
        Vehicle(-120, 3000)


def test_vehicle_negative_kms():
    with pytest.raises(ValueError):
        Vehicle(100, -100)
