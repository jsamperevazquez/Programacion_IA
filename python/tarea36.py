divisas = {'Euro': '€', 'Dollar': '$', 'Yen': '¥'}


def show_div(div):
    user_div = input("Introduce divisa\n")
    if user_div in div.keys():
        print(div[user_div])
    else:
        print(f"{user_div} no se encuentra en diccionario")


show_div(divisas)

