

def prime_num(n):
    if n < 2:
        return False
    for i in range(2, int(n/2) + 1):
        if n % i == 0:
            return False
    return True


def prime_lst(lista):
    return [n for n in lista if prime_num(n)]


list_num = [1, 2, 3, 4, 5, 6, 7, 8, 10, 11]
print(prime_lst(list_num))


