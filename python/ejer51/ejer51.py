import random
import secrets
import sys
import time


class Black_jack:
    CARDS = {'K': 10, 'A': 0}
    player_values = []
    player_cards = {}
    home_values = []
    home_cards = {}

    def __init__(self, player_game):
        self.player = player_game
        print(f"Bienvenido al juego del Black Jack {self.player.player_name}")
        print("Recuerde jugar con responsabilidad y solo si es mayor de edad")
        self.give_card()

    def give_card(self):
        random_key = random.choice(list(self.CARDS.keys()))
        if random_key == "A":
            self.CARDS[random_key] = 11 if sum(self.player_values) <= 10 else 1
        key_value = self.CARDS[random_key]
        self.player_values.append(key_value)
        print(f"Te ha salido: {random_key}")
        self.check_sum_card(self.player_values)
        self.choose_card()

    def choose_card(self):
        option = input("Desea otra Carta? Y o N \n").lower()
        if option == "y":
            self.give_card()
        else:
            print(f"Te has plantado con la cantidad de {sum(self.player_values)}\n"
                  f"Turno de la casa")
            self.home_turn()

    def check_sum_card(self, cards_value):
        if sum(cards_value) > 21:
            print(f"La suma es {sum(cards_value)}, gana la casa!!")
            print(f"Tus cartas: {self.player_values}")
            sys.exit()
        print(f"La suma de tus cartas es {sum(cards_value)}")
        self.choose_card()

    def home_turn(self):
        random_home_key = random.choice(list(self.CARDS.keys()))
        if random_home_key == "A":
            self.CARDS[random_home_key] = 11
        random_home_value = self.CARDS[random_home_key]
        self.home_values.append(random_home_value)
        print(f"Ha salido: {random_home_key}, la casa suma: {sum(self.home_values)}")
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
              f"{self.player.player_name}: {self.player_values}")
        self.check_winner(sum(self.player_values), sum(self.home_values))

    @staticmethod
    def check_winner(player_sum, home_sum):
        if home_sum > 21:
            print("ENHORABUENA, has ganado a la casa!!!")
            print(f"La casa: {home_sum}\n"
                  f"Jugador: {player_sum}")
            sys.exit()
        if player_sum > home_sum:
            print("ENHORABUENA, has ganado a la casa!!!")
            print(f"La casa: {home_sum}\n"
                  f"Jugador: {player_sum}")
            sys.exit()
        else:
            print(f"La casa gana con {home_sum}")
            print(f"La casa: {home_sum}\n"
                  f"Jugador: {player_sum}")
            sys.exit()


class player:
    def __init__(self, player_name, age):
        self.player_name = player_name
        if age < 18:
            raise ValueError("La edad mínima para jugar en España son 18")
        self.age = age


player_1 = player("Angel", 21)
game_1 = Black_jack(player_1)


