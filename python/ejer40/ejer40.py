import unittest as test


def sum_num(num1):
    return num1 * (num1 + 1) / 2


if __name__ == "__main__":
    print(sum_num(int(input("Introduce un numero\n"))))
