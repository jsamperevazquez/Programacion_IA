
price_fruit = {
    'Plátano': 1.35,
    'Mazá': 0.80,
    'Pera': 0.85,
    'Laranxa': 0.70
}


def cal_price(fr, kg):
    if fr in price_fruit.keys():
        return kg * price_fruit[fr]
    else:
        return f"{fr} no está disponible"


print(cal_price(input("Introduce fruta\n"), int(input("Introduce kilos\n"))))
