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

board = np.array([[None, None, None], [None, None, None], [None, None, None]])
token_1 = "X"
token_2 = "O"


def update_board():
    pass


def check_winner():
    pass


print(board)

