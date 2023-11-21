def cal_factor(num):
    if num <= 1:
        return 1
    else:
        fact = 1
        i = 1
        while i <= num:
            fact = fact * i
            i += 1
    return fact


print(cal_factor(int(input("Introduce un numero\n"))))
