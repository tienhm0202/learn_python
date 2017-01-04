from games.treasure_hunting.equipments import Helmet


def test_level_up_item():
    item = Helmet("Mu tu than", h=1, a=2, d=3, hpl=1, apl=2, dpl=3)
    item.level_up()

    assert item.level == 2
    assert item.h == 2
    assert item.a == 4
    assert item.d == 6
