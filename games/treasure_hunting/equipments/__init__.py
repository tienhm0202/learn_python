class Equipment(object):
    """
    Characters equipments
    """
    MAX_LEVEL = 10

    def __init__(self, name=None):
        self.name = name  # Equipment's name
        self.s = 0  # Equipment's added strength
        self.a = 0  # Equipment's added agility
        self.i = 0  # Equipment's added intelligent
        self.level = 1  # Equipment's level
        self.s_per_level = 5  # added strength per level
        self.a_per_level = 5  # added agility per level
        self.i_per_level = 5  # added intelligent per level
        self.price = 0

    def level_up(self):
        """When level up, add character's point"""
        self.s += self.s_per_level
        self.a += self.a_per_level
        self.i += self.i_per_level


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
