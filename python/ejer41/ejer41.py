import math


def calc_area(r):
    return math.pi * r ** 2


def calc_vol(area, h):
    return (area * h).__round__(2)


if __name__ == "__main__":
    print(calc_vol(calc_area(float(input("Radio de circulo\n"))), float(input("Introduce altura\n"))))
