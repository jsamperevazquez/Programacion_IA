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

board = [['0', '1', '2'], ['3', '4', '5'], ['6', '7', '8']]
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

player = ["X", "O"]
turn = 0


def start_game(start_board):
    print(f"Bienvenidos al juegos del tres en raya")
    for i in start_board:
        print(i)
    choose_position(start_board, player[0])


def update_board(board_up, position, token_p):
    for i in board_up:
        if position in i:
            i[i.index(position)] = token_p
            break
    show_board(board_up, token_p)


def choose_position(board_p, player_p):
    global turn
    position = str(input(f"Seleccione la posición de la ficha {player_p} \n"))
    for i in board_p:
        if position in i:
            turn = 1 if turn == 0 else 0
            update_board(board_p, position, player_p)
            break


def check_winner(board_to_check, player_w):
    for c in WINNER_COMBOS:
        values = [board_to_check[row][col] for row, col in
                  [(c[0] // 3, c[0] % 3), (c[1] // 3, c[1] % 3), (c[2] // 3, c[2] % 3)]]
        if all(val == player_w for val in values):
            return True
    return False


def check_draw(board_to_check_draw):
    counter = 0
    for i in board_to_check_draw:
        for j in i:
            if j == 'X' or j == 'O':
                counter += 1

    if counter == 9 and not check_winner(board_to_check_draw, 'X') and not check_winner(board_to_check_draw, 'O'):
        return True
    else:
        return False


def show_board(new_board, token):
    for i in new_board:
        print(i)
    if check_draw(new_board):
        print("EMPATE!!!")
    else:
        if check_winner(new_board, token):
            print(f'¡{token} ha ganado!')
        else:
            choose_position(new_board, player[turn])


if __name__ == "__main__":
    start_game(board)


