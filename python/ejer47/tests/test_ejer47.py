from ejer47 import check_draw, check_winner

draw = [['X', 'O', 'O'],
        ['O', 'X', 'X'],
        ['X', 'O', 'O']]
winner = [['X', 'O', 'X'],
          ['O', 'X', 'O'],
          ['X', 'O', 'X']]
player = 'X'


def test_check_draw():
    assert check_draw(draw)

    assert not check_draw(winner)


def test_check_winner():
    assert check_winner(winner, player)
    assert not check_winner(draw, player)
