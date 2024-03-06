
from blackjack.baraja import nuevaBaraja


def test_baraja():
    baraja = nuevaBaraja()
    assert len(baraja._cartas) == 52


def test_barallar():
    baraja = nuevaBaraja()

    orden_cartas = baraja._cartas.copy()
    baraja.barallar()
    assert orden_cartas != baraja._cartas


def test_coger():
    baraja = nuevaBaraja()
    baraja.barallar()
    primera_carta = baraja._cartas[-1]
    lonxitude_antes = len(baraja._cartas)
    carta_collida = baraja.coger()
    lonxitude_despois = len(baraja._cartas)
    assert primera_carta == carta_collida
    assert lonxitude_antes == lonxitude_despois + 1
