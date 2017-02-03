from math import floor
from random import randint
from statistics import mean


class Monsters(object):
    def __init__(self, name, h, d, a):
        self.name = name
        self.h = h
        self.d = d
        self.a = a
        self.exp = floor(mean([h, d, a]))
        self.gold = h + d + a


class MonsterFactory:
    @classmethod
    def create_monsters(cls, character):
        """
        Create balancing monsters list for a fight
        :param character: character to fight
        """
        numbers = randint(1, 3)
