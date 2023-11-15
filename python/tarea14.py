age = int(input("Introduce tu edad\n"))

if age < 16:
    print("Te libras por ahora")
else:
    salary = int(input("Introduce tu salario\n"))
    if salary > 1000:
        print("Tienes que tributar")
    else:
        print("Tú pobre hombre no tributes")
