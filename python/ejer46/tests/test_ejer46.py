from ejer46 import search_estates


def test_search_estates():
    test_list = [{'ano': 2020, 'metros': 160, 'habitacións': 3, 'garaxe': True, 'zona': 'A'},
                 {'ano': 2022, 'metros': 280, 'habitacións': 2, 'garaxe': True, 'zona': ' B'},
                 {'ano': 1999, 'metros': 540, 'habitacións': 4, 'garaxe': True, 'zona': 'A'}]
    assert ([{'ano': 2020, 'metros': 160, 'habitacións': 3, 'garaxe': True, 'zona': 'A', 'prezo': 187997.2}]
            == search_estates(test_list, 190000))
