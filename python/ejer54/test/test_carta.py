
from blackjack.baraja import Carta


def test_cartanormal():
    carta = Carta("Diamantes", 10)
    assert carta.palo == "Diamantes"
    assert carta.numero == 10
