from ejer45 import even_odd


def test_even_odd():
    test_lst = [1, 2, 3, 4, 5, 6, 7]
    assert [2, 4, 6] == list(filter(even_odd, test_lst))
