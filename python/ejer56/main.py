from alien_regreso import *
from simple_alien import SimpleAlien

if __name__ == '__main__':
    alien = SimpleAlien(10, 5, 20)
    alien2 = SimpleAlien(13, 11, 50)
    alien1 = Decorator(alien)
    alien_personal = PersonalDeflector(alien1)
    alien_combat = CombatShield(alien2)
    print(alien_personal.hit(10))
    print(alien_personal.hit(10))
