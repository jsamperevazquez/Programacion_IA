from alien import Alien


class SimpleAlien(Alien):
    alien_count: int = 0

    def __init__(self, x, y, health=3):
        self.x = x
        self.y = y
        self.health = health
        SimpleAlien.alien_count += 1

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


def alien_creator(start_positions: list[tuple]) -> list[SimpleAlien]:
    alien_list = [SimpleAlien(position[0], position[1]) for position in start_positions]
    return alien_list


if __name__ == '__main__':
    try:
        alien_start_positions = [(4, 7), (-1, 0)]
        aliens = alien_creator(alien_start_positions)
        for alien in aliens:
            print(f"Coordenadas de aliens: X: {alien.x}, Y: {alien.y}")
    except ValueError as e:
        print(f"No se puede tener 0 o menos vidas {e}")
