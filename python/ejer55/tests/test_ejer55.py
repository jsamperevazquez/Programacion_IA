import unittest

from Alien import Alien, alien_creator


def test_alien_create():
    alien = Alien(2, 4)
    assert 2 == alien.x
    assert 4 == alien.y


def test_alien_move():
    alien = Alien(2, 4)
    assert (8, 7) == alien.teleporting(8, 7)


def test_is_alive():
    alien = Alien(2, 4)
    assert True == alien.is_alive()


def test_alien_hit():
    alien = Alien(2, 4)
    assert 1 == alien.hit(2)


def test_alien_creator():
    alien_start_positions = [(7, 2), (-4, 8)]
    aliens = alien_creator(alien_start_positions)
    assert 2 == len(aliens)
    assert 7 == aliens[0].x
    assert 8 == aliens[1].y