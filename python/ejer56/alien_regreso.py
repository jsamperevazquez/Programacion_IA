from decorator import Decorator


class PersonalDeflector(Decorator):

    def hit(self, discount_health: int = 1):
        return self._decorate.hit(discount_health - 5)


class CombatShield(Decorator):

    def hit(self, discount_health: int = 1):
        return self._decorate.hit(discount_health - 20)
