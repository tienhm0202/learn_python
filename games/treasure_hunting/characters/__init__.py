from math import floor

from games.treasure_hunting import equipments as e
from games.treasure_hunting.characters import common


ITEM_POSITION = ["helmet", "armor", "pant", "boot", "gloves", "weapon"]
MAX_INVENTORY = 100


class Characters(object):
    def __init__(self, name, priority_order=None):
        self.name = name  # character's name
        self.exp = 0  # current experience
        self.level = 1  # current level
        self.h = 100
        self.a = 100
        self.d = 100

        self.h_per_level = 5  # added hp per level
        self.a_per_level = 5  # added armor per level
        self.d_per_level = 5  # added damage per level

        self.gold = 0  # current gold

        if priority_order:
            common.balance_general_points(self, priority_order)
        # Character's equipment must be allowed
        for item_pos in ITEM_POSITION:
            setattr(self, item_pos, None)

        self.inventory = list()

    def level_up(self, times):
        """
        When level up, add character's point

        :param times: times to level up
        """
        for _ in range(0, times):
            self.level += 1
            self.h += self.h_per_level
            self.a += self.a_per_level
            self.d += self.d_per_level

    def equip_item(self, item: e.Equipment):
        """
        Equip an item in inventory
        :param item: item to equip
        """
        if item not in self.inventory:
            raise ValueError("Item not found")
        item_position = item.__class__.__name__.lower()
        setattr(self, item_position, item)
        self.h += item.h
        self.a += item.a
        self.d += item.d
        self.inventory.remove(item)

    def unequip_item(self, item_position: str):
        """
        Take off an item and put it in inventory
        :param item_position: where item is equipped
        """
        if item_position not in ITEM_POSITION:
            raise ValueError(
                "Unknown item position to un-equip %s" % item_position)

        take_off_item = getattr(self, item_position)
        setattr(self, item_position, None)
        self.h -= take_off_item.h
        self.a -= take_off_item.a
        self.d -= take_off_item.d

        self.inventory.append(take_off_item)

    def drop_item(self, item):
        """
        Remove an item from inventory
        :param item: item to remove
        """
        if item not in self.inventory:
            raise ValueError("Item not found")
        self.inventory.remove(item)

    def pick_item(self, item):
        """
        Pick up an item
        :param item: item to pick up
        """
        if len(self.inventory) == MAX_INVENTORY:
            raise ValueError("Inventory reached limits")
        self.inventory.append(item)

    def incr_exp(self, exp):
        """
        Increase character's exp
        :param exp: exp to increase
        """
        self.exp += exp
        level_to_up = floor(self.exp / 100) - self.level + 1

        if level_to_up > 0:
            self.level_up(level_to_up)

    def pick_gold(self, amount):
        """
        Pick up amount of golds
        :param amount: amount of golds
        """
        self.gold += amount

    def buy_item(self, item: e.Equipment):
        """
        Buy an item
        :param item: item to buy
        """
        if self.gold < item.price:
            raise ValueError("Not enough gold to buy it")

        self.gold -= item.price
        self.inventory.append(item)


class Warriors(Characters):
    def __init__(self, name):
        priority_order = ["h", "a", "d"]
        super(Warriors, self).__init__(name, priority_order)


class Hunters(Characters):
    def __init__(self, name):
        priority_order = ["a", "d", "h"]
        super(Hunters, self).__init__(name, priority_order)


class Wizards(Characters):
    def __init__(self, name):
        priority_order = ["d", "h", "a"]
        super(Wizards, self).__init__(name, priority_order)

