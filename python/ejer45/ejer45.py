list_num = [1, 2, 3, 4, 5, 6, 7, 8]

# Con lambda
list_odd = list(filter(lambda n: n % 2 == 0, list_num))

print(f"Con función lambda: {list_odd}")

# Con listcomprehesion
list_odd_compreh = [x for x in list_num if x % 2 == 0]

print(f"Con comprensión de listas: {list_odd_compreh}")

# Con ternarios y comprensión
even_odd_list = ['Par' if x % 2 == 0 else 'Impar' for x in list_num]

print(f"Usando ternarios en comprensión: {even_odd_list}")


# Con función filter
def even_odd(n):
    if n % 2 == 0:
        return True


list_map = list(filter(even_odd, list_num))
print(f"Usando la función filter: {list_map}")
