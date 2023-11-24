list_num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list_num.sort(reverse=True)
separator = ","


def separate_list(l_num):
    for i in range(len(l_num)):
        l_num[i] = str(l_num[i])
    return l_num


print(separator.join(separate_list(separate_list(list_num))))
