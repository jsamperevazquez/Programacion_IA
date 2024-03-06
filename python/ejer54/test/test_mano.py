from blackjack.baraja import Carta, Mano


def test_mano():
    carta = Carta("Diamantes", 10)
    carta2 = Carta("Diamantes", 'K')
    mano = Mano()
    mano.addCarta(carta)
    mano.addCarta(carta2)

    assert mano.puntos == 20


def test_blackjack():
    mano = Mano()
    mano.addCarta(Carta("Diamantes", 10))
    mano.addCarta(Carta("Diamantes", 'A'))

    assert mano.puntos == 21


def test_dosas():
    mano = Mano()
    mano.addCarta(Carta("Diamantes", 10))
    mano.addCarta(Carta("Diamantes", 'A'))
    mano.addCarta(Carta("Picas", 'A'))

    assert mano.puntos == 12


def test_dosas2():
    mano = Mano()
    mano.addCarta(Carta("Diamantes", 9))
    mano.addCarta(Carta("Diamantes", 'A'))
    mano.addCarta(Carta("Picas", 'A'))

    assert mano.puntos == 21


def test_pasado():
    mano = Mano()
    mano.addCarta(Carta("Diamantes", 9))
    mano.addCarta(Carta("Diamantes", 4))
    mano.addCarta(Carta("Picas", 10))

    assert mano.puntos == 23


def test_ace():
    carta = Carta("Diamantes", 'A')
    mano = Mano()
    mano.addCarta(carta)

    assert mano.puntos == 11


def test_2ace():
    carta = Carta("Diamantes", 'A')
    carta2 = Carta("Picas", 'A')
    mano = Mano()
    mano.addCarta(carta)
    mano.addCarta(carta2)

    assert mano.puntos == 12


def test_muchas():
    mano = Mano()
    mano.addCarta(Carta("Diamantes", 4))
    mano.addCarta(Carta("Diamantes", 'Q'))
    mano.addCarta(Carta("Diamantes", 'A'))
    mano.addCarta(Carta("Diamantes", 2))
    mano.addCarta(Carta("Diamantes", 'J'))

    assert mano.puntos > 21
    assert mano.puntos == 27
