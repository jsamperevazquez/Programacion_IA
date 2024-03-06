class Alien:
    x: list
    y: list
    salud: int

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.salud = 3

    def hit(self, salud_descontar=1):
        self.salud -= salud_descontar if salud_descontar != 1 else 1

    def is_alive(self):
        return True if self.salud > 0 else False

    def teleporting(self, x_teleport: list, y_teleport: list):
        self.x = x_teleport
        self.y = y_teleport


alien1 = Alien([2, 1], [4, 3])
alien1.hit()
print(f"salud Alien: {alien1.salud}")
print(alien1.is_alive())
alien1.teleporting([4, 1], [7, 4])
print(f"{alien1.x} , {alien1.y}")
