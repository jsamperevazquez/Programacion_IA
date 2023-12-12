from datetime import date

estate_lst = [{'ano': 2000, 'metros': 100, 'habitacións': 3, 'garaxe': True, 'zona': 'A'},
              {'ano': 2012, 'metros': 60, 'habitacións': 2, 'garaxe': True, 'zona': ' B'},
              {'ano': 1980, 'metros': 120, 'habitacións': 4, 'garaxe': False, 'zona': 'A'},
              {'ano': 2005, 'metros': 75, 'habitacións': 3, 'garaxe': True, 'zona': ' B'},
              {'ano': 2015, 'metros': 90, 'habitacións': 2, 'garaxe': False, 'zona': 'A'}]
YEAR = date.today().year


def calculate_price(estates):
    for i in estates:
        match i['zona']:
            case 'A':
                if i['garaxe']:
                    i['prezo'] = ((i['metros'] * 1000 + i['habitacións'] * 5000 + 15000) *
                                  (1 - (YEAR - i['ano']) / 100)).__round__(1)
                else:
                    i['prezo'] = ((i['metros'] * 1000 + i['habitacións'] * 5000) *
                                  (1 - (YEAR - i['ano']) / 100)).__round__(1)
            case ' B':
                if i['garaxe']:
                    i['prezo'] = (i['metros'] * 1000 + i['habitacións'] * 5000 + 15000 *
                                  (1 - (YEAR - i['ano']) / 100)) * 1.5.__round__(1)
                else:
                    i['prezo'] = (i['metros'] * 1000 + i['habitacións'] * 5000 *
                                  (1 - (YEAR - i['ano']) / 100)) * 1.5.__round__(1)
    return estates


def search_estates(estates, amount):
    est_less = [x for x in calculate_price(estates) if x['prezo'] < amount]
    return est_less


print(search_estates(estate_lst, 180000))
