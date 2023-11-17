number = int(input("Introduce un número\n"))

for i in range(2, number):
    if number % i == 0:
        print(f"{number} no es primo")
        break
else:
    print(f"{number} es primo")


