estate_lst = [{'ano': 2000, 'metros': 100, 'habitacións': 3, 'garaxe': True, 'zona': 'A'},
              {'ano': 2012, 'metros': 60, 'habitacións': 2, 'garaxe': True, 'zona': ' B'},
              {'ano': 1980, 'metros': 120, 'habitacións': 4, 'garaxe': False, 'zona': 'A'},
              {'ano': 2005, 'metros': 75, 'habitacións': 3, 'garaxe': True, 'zona': ' B'},
              {'ano': 2015, 'metros': 90, 'habitacións': 2, 'garaxe': False, 'zona': 'A'}]

"""
Cree una función que le permita buscar propiedades en función de un presupuesto determinado. La función tomará como 
entrada la lista de propiedades y un precio, y devolverá otra lista con las propiedades cuyo precio 
sea menor o igual al dado.
Las propiedades del listado que se devuelve deben incorporar un nuevo atributo de cada diccionario
con el precio de la propiedad, donde el precio de una propiedad se calcula con la siguiente fórmula dependiendo
de la zona:
Zona A: prezo = (metros * 1000 + habitacións * 5000 + garaxe * 15000) * (1- antiguedad/100)
Zona  B: prezo = (metros * 1000 + habitacións * 5000 + garaxe * 15000) * (1- antiguedad/100) * 1.5
"""


def calculate_price(estates):
    match estates['zona']:
        case 'A':
            if estates['garaxe']:
                estates['prezo'] = (estates['metros'] * 1000 + estates['habitacións'] * 5000 * 15000 *
                                    (1 - estates['antiguedad'] / 100))
            else:
                estates['prezo'] = (estates['metros'] * 1000 + estates['habitacións'] * 5000 *
                                    (1 - estates['antiguedad'] / 100))


calculate_price(estate_lst)
