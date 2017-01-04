from math import floor
from statistics import mean


class Monsters(object):
    def __init__(self, name, h, d, a):
        self.name = name
        self.h = h
        self.d = d
        self.a = a
        self.exp = floor(mean([h, d, a]))
        self.gold = h + d + a
