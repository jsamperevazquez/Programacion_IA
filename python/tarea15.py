"""
Os alumnos dun curso dividíronse en dous grupos A e  B de acordo ao sexo e o nome.
O grupo A esta formado polas mulleres cun nome anterior á  M
e os homes cun nome posterior á  N e o grupo  B polo resto.
Escribir un programa que pregunte ao usuario o seu nome e sexo,
e mostre por pantalla o grupo que lle corresponde.
"""

# User name
user_name = input("Introduce tu nombre\n")
# First Character to evaluate
list_c = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "k", "l", "m", "n"]
# User gender
gen = input("Introduce tu sexo: M o F\n").lower()

# Bucle for two possibilities
while True:
    if gen == "m" or gen == "f":
        break
    else:
        gen = input("Sexo inválido, introduce tu sexo: M o F\n").lower()

# match case to evaluate the cases (3.10 minimum needed)
match gen.lower():
    case "m":
        if user_name[0].lower() not in list_c:
            print(f"{user_name} estás en el grupo A")
        else:
            print(f"{user_name} estás en el grupo B")
    case "f":
        if user_name[0].lower() in list_c[:-2]:
            print(f"{user_name} estás en el grupo A")
        else:
            print(f"{user_name} estás en el grupo B")

