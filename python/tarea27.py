def cal_imp(a, t=21):
    if not t:
        t = int(21)
    else:
        t = int(t)
    val = a + (a * t / 100)
    print(f"El total es de {val} €")


cal_imp(float(input("Introduce cantidad\n")), input("Introduce porcentaje a aplicar"))
