CLOWN_W = 112
DOLL_W = 75


def cal_weight():
    cl = int(input("Introduce el número de payasos vendidos\n"))
    do = int(input("Introduce el número de muñecas vendidas\n"))
    pack = cl * CLOWN_W / 100 + do * DOLL_W / 100
    return pack


print(cal_weight())