def balance_general_points(characters, priority_order: list):
    """
    Balance character's general point by its priority order
    :param characters: character
    :param priority_order: should be order of h, a and d as character HP,
    Armor, Damage
    """
    setattr(characters, priority_order[0], 20)
    setattr(characters, priority_order[1], 15)
    setattr(characters, priority_order[2], 10)

    setattr(characters, priority_order[0] + "_per_level", 5)
    setattr(characters, priority_order[1] + "_per_level", 2)
    setattr(characters, priority_order[2] + "_per_level", 1)
