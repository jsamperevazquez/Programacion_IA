from ejer46 import search_estates, estate_lst


def test_search_estates():
    assert ([  # {'ano': 2000, 'metros': 100, 'habitacións': 3, 'garaxe': True, 'zona': 'A', 'prezo': 100100.0}
                # , {'ano': 2012, 'metros': 60, 'habitacións': 2, 'garaxe': True, 'zona': ' B', 'prezo': 125025.0}
                {'ano': 1980, 'metros': 120, 'habitacións': 4, 'garaxe': False, 'zona': 'A', 'prezo': 79800.0}
                # , {'ano': 2005, 'metros': 75, 'habitacións': 3, 'garaxe': True, 'zona': ' B', 'prezo': 153450.0}
                , {'ano': 2015, 'metros': 90, 'habitacións': 2, 'garaxe': False, 'zona': 'A', 'prezo': 92000.0}]

            == search_estates(estate_lst, 100000))
