
list_double = []


def sqrt_num(n):
    return n ** 2


def execute_func(fun, *args):
    for n in args:
        list_double.append(fun(n))
    return list_double


execute_func(sqrt_num, 2, 4)
print(list_double)



