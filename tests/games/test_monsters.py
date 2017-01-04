from games.treasure_hunting.monsters import Monsters


def test_new_monster():
    monster = Monsters("Ga Con", 1, 1, 1)
    assert monster.h == monster.a == monster.d == 1
    assert monster.exp == 1
    assert monster.gold == 3

    monster = Monsters("Ga Cha", 1, 2, 3)
    assert monster.exp == 2
    assert monster.gold == 6

    monster = Monsters("Ga Me", 1, 2, 2)
    assert monster.exp == 1
    assert monster.gold == 5
