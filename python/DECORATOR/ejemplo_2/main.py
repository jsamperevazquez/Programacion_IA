from concrete_decorator import *
from concrete_component import XogadorIni

if __name__ == "__main__":
    x = XogadorIni()
    print(x.ataque())
    print(x.defensa())
    print(x.vida)

    a = Decorator(x)
    print(a.ataque())
    print(a.defensa())
    print(a.vida)

    b = Martillo(x)
    print(b.ataque())
    print(b.defensa())
    print(b.vida)

    superPoderoso = AnilloDeLaIra(Escudo(Martillo(x)))
    print(superPoderoso.ataque())
    print(superPoderoso.defensa())
