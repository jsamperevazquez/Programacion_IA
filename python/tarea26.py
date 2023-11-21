def calc_imc():
    weight = float(input("Introduce tu peso en Kg\n"))
    height = float(input("Introduce tu altura en Cms\n"))
    imc = weight / (height / 100) ** 2
    print(f"Tu índice de masa corporal es {imc.__round__(2)}")


calc_imc()
