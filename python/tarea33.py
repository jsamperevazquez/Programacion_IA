num_loto = []


def show_winfo(list_num):
    return sorted(list_num)


for i in range(6):
    num_loto.insert(i, int(input("Introduce numero ganador\n")))


print(show_winfo(num_loto))
