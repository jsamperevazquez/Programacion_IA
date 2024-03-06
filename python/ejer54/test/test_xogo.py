
from blackjack.xogo import Xogador, Xogo
from blackjack.baraja import Carta, Baraja


def test_xogo1():
    xogador = Xogador("Xogador1")
    xogador2 = Xogador("Xogador2")
    xogador3 = Xogador("Xogador3")
    baraja = Baraja()
    baraja.addCarta(Carta('Diamantes', 10))
    baraja.addCarta(Carta('Diamantes', 5))
    baraja.addCarta(Carta('Picas', 6))
    baraja.addCarta(Carta('Diamantes', 10))
    baraja.addCarta(Carta('Diamantes', 5))
    baraja.addCarta(Carta('Picas', 6))
    baraja.addCarta(Carta('Diamantes', 10))
    baraja.addCarta(Carta('Diamantes', 5))
    baraja.addCarta(Carta('Picas', 10))

    xogador.actuar('pedir', baraja)
    xogador.actuar('pedir', baraja)
    assert xogador.puntos == 15
    assert xogador.podePedir() is True
    assert xogador.podeGanhar() is True
    xogador.actuar('pedir', baraja)
    assert xogador.puntos == 25
    assert xogador.podePedir() is False
    assert xogador.podeGanhar() is False

    xogador2.actuar('pedir', baraja)
    xogador2.actuar('pedir', baraja)
    xogador2.actuar('pedir', baraja)
    assert xogador2.puntos == 21
    xogador2.actuar('plantarse', baraja)
    assert xogador2.podePedir() is False
    assert xogador2.podeGanhar() is True

    xogador3.actuar('pedir', baraja)
    xogador3.actuar('pedir', baraja)
    assert xogador3.puntos == 11
    xogador3.actuar('plantarse', baraja)
    assert xogador3.podePedir() is False
    assert xogador3.podeGanhar() is True

    xogo = Xogo()
    xogo.addXogador(xogador)
    xogo.addXogador(xogador2)
    xogo.addXogador(xogador3)

    ganhador = xogo.ganhador()
    assert len(ganhador) == 1
    assert ganhador[0].nome == 'Xogador2'


def test_xogo2():
    xogador = Xogador("Xogador1")
    xogador2 = Xogador("Xogador2")
    xogador3 = Xogador("Xogador3")
    baraja = Baraja()
    baraja.addCarta(Carta('Diamantes', 10))
    baraja.addCarta(Carta('Diamantes', 5))
    baraja.addCarta(Carta('Picas', 'Q'))
    baraja.addCarta(Carta('Diamantes', 10))
    baraja.addCarta(Carta('Diamantes', 5))
    baraja.addCarta(Carta('Picas', 'K'))
    baraja.addCarta(Carta('Diamantes', 10))
    baraja.addCarta(Carta('Diamantes', 5))
    baraja.addCarta(Carta('Picas', 10))

    xogador.actuar('pedir', baraja)
    xogador.actuar('pedir', baraja)
    assert xogador.puntos == 15
    assert xogador.podePedir() is True
    assert xogador.podeGanhar() is True
    xogador.actuar('pedir', baraja)
    assert xogador.puntos == 25
    assert xogador.podePedir() is False
    assert xogador.podeGanhar() is False

    xogador2.actuar('pedir', baraja)
    xogador2.actuar('pedir', baraja)
    xogador2.actuar('pedir', baraja)
    assert xogador2.puntos == 25
    assert xogador2.podePedir() is False
    assert xogador2.podeGanhar() is False

    xogador3.actuar('pedir', baraja)
    xogador3.actuar('pedir', baraja)
    xogador3.actuar('pedir', baraja)
    assert xogador3.puntos == 25
    assert xogador3.podePedir() is False
    assert xogador3.podeGanhar() is False

    xogo = Xogo()
    xogo.addXogador(xogador)
    xogo.addXogador(xogador2)
    xogo.addXogador(xogador3)

    ganhador = xogo.ganhador()
    assert len(ganhador) == 0
    # assert ganhador[0].nome == 'Xogador2'


def test_xogo3():
    xogador = Xogador("Xogador1")
    xogador2 = Xogador("Xogador2")
    xogador3 = Xogador("Xogador3")
    baraja = Baraja()
    baraja.addCarta(Carta('Diamantes', 10))
    baraja.addCarta(Carta('Diamantes', 'A'))
    baraja.addCarta(Carta('Picas', 'K'))
    baraja.addCarta(Carta('Diamantes', 10))
    baraja.addCarta(Carta('Diamantes', 5))
    baraja.addCarta(Carta('Picas', 6))
    baraja.addCarta(Carta('Diamantes', 10))
    baraja.addCarta(Carta('Diamantes', 5))
    baraja.addCarta(Carta('Picas', 10))

    xogador.actuar('pedir', baraja)
    xogador.actuar('pedir', baraja)
    assert xogador.puntos == 15
    assert xogador.podePedir() is True
    assert xogador.podeGanhar() is True
    xogador.actuar('pedir', baraja)
    assert xogador.puntos == 25
    assert xogador.podePedir() is False
    assert xogador.podeGanhar() is False

    xogador2.actuar('pedir', baraja)
    xogador2.actuar('pedir', baraja)
    xogador2.actuar('pedir', baraja)
    assert xogador2.puntos == 21
    xogador2.actuar('plantarse', baraja)
    assert xogador2.podePedir() is False
    assert xogador2.podeGanhar() is True

    xogador3.actuar('pedir', baraja)
    xogador3.actuar('pedir', baraja)
    assert xogador3.puntos == 21
    xogador3.actuar('plantarse', baraja)
    assert xogador3.podePedir() is False
    assert xogador3.podeGanhar() is True

    xogo = Xogo()
    xogo.addXogador(xogador)
    xogo.addXogador(xogador2)
    xogo.addXogador(xogador3)

    ganhador = xogo.ganhador()
    assert len(ganhador) == 2
    assert ganhador[0].nome == 'Xogador2'
    assert ganhador[1].nome == 'Xogador3'
