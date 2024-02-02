"""
Imos a implementar o xogo do tres en raia. Para iso imos a ir por partes.
Lembra que o tablero é de 3 x 3. Fara representalo quizais sexa o mellor representalo cunha lista de listas.
- Inicializa a estrutura a baleiro.
- Imprime o taboleiro.
- Podes facer que X represente unha ficha do xogador 1 e O a do xogador 2
- Fai unha función que nos indique se temos un gañador ou non.
- Utiliza test para comprobar os casos posibles, non teñen que ser todos, pero algúns si.
- Implementa agora o proceso de xogo:
    - Primeiro un xogador, comproba se hai gañador, logo outro.
    - Paras cando un gaña ou xa non hai máis movementos.
"""
import numpy as np

board = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
WINNER_COMBOS = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6],
]
token_1 = "X"
token_2 = "O"


def update_board(board_up):
    pass


def check_winner(board_to_check):
    pass


def show_board(new_board):
    for i in new_board:
        print(i)

    position = int(input("Introduce posición en el tablero\n"))
    new_board[0][position] = token_1
    update_board(new_board)
    check_winner(new_board)
    show_board(new_board)


show_board(board)

