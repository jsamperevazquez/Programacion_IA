shop_bask = {}
continue_shop = True


def make_bask(art, price):
    global continue_shop
    try:
        while continue_shop:
            shop_bask[art] = price
            make_bask(input("Introduce Artículo..., ENTER para terminar\n"),
                      float(input("Introduce precio Artículo\n")))
    except ValueError:
        print(f"Gracias por usar nuestros servicios\n"
              f"\n\t {'*' * 9}  TICKET {'*' * 9}\n")
        continue_shop = False
        show_bask(shop_bask)


def show_bask(bask):
    total = 0
    for k, v in bask.items():
        total += v
        print(f"{k:10}------{v:>6}\n")
    print(f"TOTAL{total:>18}")


try:
    make_bask(input("Introduce Artículo..., ENTER para terminar\n"),
              float(input("Introduce precio Artículo\n")))
except ValueError:
    print("Gracias por la visita")
