number = int(input("Introduce un número\n"))
number_list = []
for i in range(number + 1):
    number_list.append(number)
    number -= 1

print(number_list)
