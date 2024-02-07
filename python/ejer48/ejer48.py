def validate_number(number):
    if number <= 9:
        raise_exception()
    count = 1
    while number > 9:
        number = number // 10
        count += 1
    print(f"Tiene {count} dígitos")


def raise_exception():
    raise ValueError("Número inválido")


class users:
    def __init__(self, name, user_name, password, key_number=None):
        self.name = name
        self.user_name = user_name
        self.password = password
        self.key_number = key_number
        if key_number is not None:
            validate_number(self.key_number)


user1 = users('Angel', user_name='Ritrux', password='<PASSWORD>', key_number=12345678)

