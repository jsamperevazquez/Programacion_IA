password = input("Introduce la contraseña\n")
PASS = str("1234")

while True:
    if password.__eq__(PASS):
        print("Contraseña correcta")
        break
    else:
        password = input("Contraseña incorreta, vuelva a introducir\n")
