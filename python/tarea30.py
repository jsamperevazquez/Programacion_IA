import math


def calc_area():
    rad = float(input("Radio de circulo\n"))
    return math.pi * rad ** 2


def calc_vol(area):
    h = float(input("Introduce altura del cilindro\n"))
    return (area * h).__round__(2)


print(calc_vol(calc_area()))
