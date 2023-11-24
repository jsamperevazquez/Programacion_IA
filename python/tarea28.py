def rest_quotient(n1, n2):
    try:
        num_tup = (n1 // n2, n1 % n2)
        return num_tup
    except ZeroDivisionError as t:
        print(f"No se puede dividir por {n2}", type(t).__name__)
        print(rest_quotient(int(input("Introduce un numero entero\n")), int(input("Introduce otro número\n"))))

    except TypeError as t:
        print(f"Tipo de dato incorrecto", type(t).__name__)


try:
    print(rest_quotient(int(input("Introduce un numero entero\n")), int(input("Introduce otro número\n"))))
except ValueError as e:
    print(f"Tipo de dato incorrecto", type(e).__name__)
    print(rest_quotient(int(input("Introduce un numero entero\n")), int(input("Introduce otro número\n"))))
