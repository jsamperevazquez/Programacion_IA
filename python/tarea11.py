password = "arameo"
user_password = input("Introduce un contraseña\n")

while True:
    if password.lower() == user_password.lower():
        break
    else:
        user_password = input("Contraseña erronea, introduce un contraseña\n")
print("Contraseña válida")
