import random
import time


class BlackJack:
    # clave valor con los valores de cada carta
    CARDS = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'J': 10, 'Q': 10, 'K': 10, 'A': 0}

    def __init__(self, player_name, age):
        self.player_name = player_name
        self.player_values = []
        self.home_values = []
        self.game_continue = True
        if age < 18:
            raise ValueError("La edad mínima para jugar en España son 18")
        self.give_card()

    def give_card(self):
        random_key = random.choice(list(self.CARDS.keys()))
        # Si la key es A escogemos el valor 1 0 11 en función de necesidad
        if random_key == "A":
            self.CARDS[random_key] = 11 if sum(self.player_values) <= 10 else 1
        key_value = self.CARDS[random_key]
        self.player_values.append(key_value)
        print(f"Te ha salido: {random_key}")
        self.check_sum_card()

    def check_sum_card(self):
        if sum(self.player_values) > 21:
            print(f"La suma es {sum(self.player_values)}, gana la casa!!")
            print(f"Tus cartas: {self.player_values}")
            self.new_game()
        print(f"La suma de tus cartas es {sum(self.player_values)}")
        self.choose_card()

    def choose_card(self):
        # Mientras el flag esté en 1 mantenemos el juego
        while self.game_continue:
            option = input("Desea otra Carta? Y o N \n").lower()
            if option == "y":
                self.give_card()
            elif option == "n":
                print(f"Te has plantado con la cantidad de {sum(self.player_values)}\n"
                      f"Turno de la casa")
                self.home_turn()
            else:
                print("Opción inválida, por favor introduce Y o N")
        return

    # Juego de la Banca
    def home_turn(self):
        while sum(self.home_values) < sum(self.player_values):
            time.sleep(2)
            random_home_key = random.choice(list(self.CARDS.keys()))
            if random_home_key == "A":
                self.CARDS[random_home_key] = 11 if sum(self.home_values) <= 10 else 1
            random_home_value = self.CARDS[random_home_key]
            self.home_values.append(random_home_value)
            print(f"Ha salido {random_home_key}, la casa suma: {sum(self.home_values)}")
            time.sleep(1)
        print(f"La casa: {self.home_values}\n"
              f"{self.player_name}: {self.player_values}")
        self.check_winner(self.player_values, self.home_values)

    def check_winner(self, val_player, val_home):
        if sum(val_home) > 21 or sum(val_player) > sum(val_home):
            print("ENHORABUENA, has ganado a la casa!!!")
        elif val_home >= val_player:
            print(f"La casa gana con {sum(val_home)}")
        self.new_game()

    def new_game(self):
        while True:
            res = input("Desea volver a jugar?? Y o N\n").lower()
            if res == "y":
                self.player_values = []
                self.home_values = []
                self.give_card()
                break
            elif res == "n":
                print("Gracias por usar nuestros juegos")
                self.game_continue = False
                return
            else:
                print("Por favor ingrese Y o N")


if __name__ == '__main__':
    try:
        player_name = input("Introduce tu nombre: ")
        age = int(input("Introduce tu edad: "))
        game = BlackJack(player_name, age)
    except ValueError as e:
        print(f"No se puede iniciar el juego: {e}")

