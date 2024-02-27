from dataclasses import dataclass, field
from typing import Union


def validate_number(number):
    # Corto la cadena por cada espacio y chequeo que tengan la longitud mínima
    if len(number.split()) <= 1:
        raise_exception()
    # Elimino los espacios en blanco
    number_to = number.replace(' ', '')
    # Uso slice para crear subcadenas de posiciones pares e impares empezando por el final
    impair_pos = list(map(int, number_to[-1::-2]))
    pair_pos = list(map(int, number_to[-2::-2]))
    # Utilizo función map con lambda para doblar y restar 9 si > 9
    double_val = list(map(lambda x: x * 2, pair_pos))
    double_val = list(map(lambda x: x - 9 if x > 9 else x, double_val))
    # Concateno ambas listas
    sum_list = double_val + impair_pos
    # Compruebo si el ∑ de todos los elementos de la lista es divisible entre 10
    if sum(sum_list) % 10 == 0:
        print(f'{number} es un número válido')
        return True
    else:
        raise_exception()
    return False


def raise_exception():
    raise ValueError("Número inválido")


@dataclass()
class User:
    name: str
    surname: str
    user_name: str
    password: str
    key_number: Union[str, any]
    full_name: str = field(init=False, repr=True)

    def __post_init__(self):
        self.full_name = f"{self.name} {self.surname}"
        if self.key_number is not None:
            validate_number(self.key_number)


@dataclass(frozen=True)
class InmutableUser:
    name: str
    surname: str
    user_name: str
    password: str
    key_number: Union[str, any]

    @property
    def full_name(self) -> str:
        return f"{self.name} {self.surname}"

    def __post_init__(self):
        if self.key_number is not None:
            validate_number(self.key_number)


if __name__ == '__main__':

    user2 = User('Jose', 'Rato', 'Ratoncito', '<PASSWORD>', key_number='5256 7833 7156 7695')
