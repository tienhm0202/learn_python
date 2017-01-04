class Equipment(object):
    """
    Characters equipments
    """
    MAX_LEVEL = 10

    def __init__(self, name=None, h=0, a=0, d=0, hpl=0, apl=0, dpl=0, price=0):
        self.name = name  # Equipment's name
        self.h = h  # Equipment's added hp
        self.a = a  # Equipment's added armor
        self.d = d  # Equipment's added damage
        self.level = 1  # Equipment's level
        self.h_per_level = hpl  # added hp per level
        self.a_per_level = apl  # added armor per level
        self.d_per_level = dpl  # added damage per level
        self.price = price

    def level_up(self):
        """When level up, add character's point"""
        self.h += self.h_per_level
        self.a += self.a_per_level
        self.d += self.d_per_level
        self.level += 1


class Helmet(Equipment):
    pass


class Armor(Equipment):
    pass


class Pant(Equipment):
    pass


class Boot(Equipment):
    pass


class Gloves(Equipment):
    pass


class Weapon(Equipment):
    pass
