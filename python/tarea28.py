def rest_quotient(n1, n2):
    num_tup = (n1, "entre ", n2, "da un cociente de", n1 / n2, "e un resto de", n1 % n2)
    return num_tup


print(rest_quotient(int(input("Introduce un numero entero\n")), int(input("Introduce otro número\n"))))

