from ejer44 import prime_num, prime_lst


def test_prime_num():
    list_num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert [2, 3, 5, 7] == prime_lst(list_num)
