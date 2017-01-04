import pytest

from games.treasure_hunting.characters import Warriors, Wizards, Hunters, \
    MAX_INVENTORY
from games.treasure_hunting.equipments import Helmet


def test_new_warrior():
    warrior = Warriors("Chua")

    assert warrior.name == "Chua"
    assert warrior.level == 1
    assert warrior.h == 20
    assert warrior.a == 15
    assert warrior.d == 10

    assert warrior.h_per_level == 5
    assert warrior.a_per_level == 2
    assert warrior.d_per_level == 1


def test_new_wizard():
    wizard = Wizards("Chua")

    assert wizard.name == "Chua"
    assert wizard.level == 1
    assert wizard.h == 15
    assert wizard.a == 10
    assert wizard.d == 20

    assert wizard.h_per_level == 2
    assert wizard.a_per_level == 1
    assert wizard.d_per_level == 5


def test_new_hunter():
    hunter = Hunters("Chua")

    assert hunter.name == "Chua"
    assert hunter.level == 1
    assert hunter.h == 10
    assert hunter.a == 20
    assert hunter.d == 15

    assert hunter.h_per_level == 1
    assert hunter.a_per_level == 5
    assert hunter.d_per_level == 2


def test_level_up():
    warrior = Warriors("Chua")

    warrior.level_up(1)
    assert warrior.h == 25
    assert warrior.a == 17
    assert warrior.d == 11
    assert warrior.level == 2

    warrior.level_up(0)
    assert warrior.h == 25
    assert warrior.a == 17
    assert warrior.d == 11
    assert warrior.level == 2


def test_pick_up_item():
    item = Helmet("Mu tu than", h=1, a=1, d=1, hpl=1, apl=1, dpl=1)

    warrior = Warriors("Chua")
    warrior.pick_item(item)

    assert item in warrior.inventory

    for i in range(1, MAX_INVENTORY):
        warrior.pick_item(item)

    assert len(warrior.inventory) == 100
    with pytest.raises(ValueError) as e:
        warrior.pick_item(item)
    assert "Inventory reached limits" in str(e)


def test_equip_item():
    item = Helmet("Mu tu than", h=1, a=1, d=1, hpl=1, apl=1, dpl=1)
    warrior = Warriors("Chua")

    # Equip an item which is not picked
    with pytest.raises(ValueError) as e:
        warrior.equip_item(item)
    assert "Item not found" in str(e)

    # Pick up item and equip
    warrior.pick_item(item)
    warrior.equip_item(item)
    assert warrior.h == 21
    assert warrior.a == 16
    assert warrior.d == 11
    assert warrior.helmet == item
    assert not warrior.inventory

    # Un-equip item
    warrior.unequip_item("helmet")
    assert warrior.h == 20
    assert warrior.a == 15
    assert warrior.d == 10
    assert item in warrior.inventory

    # Un-equip unknown item
    with pytest.raises(ValueError) as e:
        warrior.unequip_item("Chim")
    assert "Unknown item position to un-equip Chim" in str(e)


def test_drop_item():
    item = Helmet("Mu tu than", h=1, a=1, d=1, hpl=1, apl=1, dpl=1)
    warrior = Warriors("Chua")

    # Drop picked item
    warrior.pick_item(item)
    warrior.drop_item(item)
    assert not warrior.inventory

    # Drop un-picked item
    with pytest.raises(ValueError) as e:
        warrior.drop_item(item)
    assert "Item not found" in str(e)

    # Drop one of many item
    warrior.pick_item(item)
    warrior.pick_item(item)
    assert warrior.inventory.count(item) == 2
    warrior.drop_item(item)
    assert len(warrior.inventory) == 1
    assert item in warrior.inventory
    assert warrior.inventory.count(item) == 1


def test_pick_up_gold():
    warrior = Warriors("Chua")

    warrior.pick_gold(100)
    assert warrior.gold == 100


def test_buy_item():
    item_expensive = Helmet("Mu tu than", price=1000)
    item_cheap = Helmet("Thit cho", price=10)

    warrior = Warriors("Chua")
    warrior.pick_gold(100)
    assert warrior.gold == 100

    warrior.buy_item(item_cheap)
    assert warrior.gold == 90
    assert item_cheap in warrior.inventory

    with pytest.raises(ValueError) as e:
        warrior.buy_item(item_expensive)
    assert "Not enough gold to buy it" in str(e)


def test_incr_exp():
    warrior = Warriors("Chua")
    warrior.incr_exp(10)
    assert warrior.exp == 10

    warrior.incr_exp(100)
    assert warrior.exp == 110
    assert warrior.level == 2