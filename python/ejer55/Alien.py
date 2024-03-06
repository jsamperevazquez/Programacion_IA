from typing import Tuple


class Alien:
    x: int
    y: int
    health: int
    alien_count: int = 0

    def __init__(self, x, y, health=3):
        self.x = x
        self.y = y
        self.health = health
        Alien.alien_count += 1

    def hit(self, discount_health=1) -> int:
        self.health -= discount_health if discount_health != 1 else 1
        if self.health <= 0:
            raise ValueError()
        return self.health

    def is_alive(self) -> bool:
        return True if self.health > 0 else False

    def teleporting(self, x_teleport: int, y_teleport: int) -> tuple[int, int]:
        self.x = x_teleport
        self.y = y_teleport
        return self.x, self.y

    def collision_detect(self, target_x: int, target_y: int) -> bool:
        if self.x == target_x and self.y == target_y:
            return True
        return False


def alien_creator(start_positions: list[tuple]) -> list[Alien]:
    alien_list = [Alien([position[0] for position in start_positions],
                        [position[1] for position in start_positions])]
    return alien_list


if __name__ == '__main__':
    try:
        alien1 = Alien(2, 1)
        alien2 = Alien(4, 8, 1)
        try:
            alien1.hit()
        except ValueError as e:
            print(f"No se puede tener 0 o menos vidas, error: {type(e).__name__}")
        try:
            alien2.hit()
        except ValueError as e:
            print(f"No se puede tener 0 o menos vidas, error: {type(e).__name__}")
        alien_creator([(4, 7), (-1, 0)])
        alien_start_positions = [(4, 7), (-1, 0)]
        aliens = alien_creator(alien_start_positions)
    except ValueError as e:
        print(f"No se puede tener 0 o menos vidas {e}")