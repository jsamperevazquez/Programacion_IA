from ejer41 import calc_vol, calc_area


def test_calc_area():
    assert calc_area(5) == 78.53981633974483


def test_calc_vol():
    assert calc_vol(calc_area(5), 5) == 392.7
