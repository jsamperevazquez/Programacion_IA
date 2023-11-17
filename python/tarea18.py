number = int(input("Introduce un número\n"))

for i in range(number + 1):
    if i % 2 != 0:
        print(f"{i} es impar")

