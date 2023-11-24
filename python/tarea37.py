user_data = {}
data = ['nombre', 'edad', 'direccion', 'telefono']


def ask_user(user_d):
    for i in range(len(user_d)):
        user_data[data[i]] = input(f"Introduce tu {data[i]}\n")
    return user_data


print(ask_user(data))

