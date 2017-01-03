from math import floor


def get_middle_element(l: list):
    """
    Get the position of the middle element of a list. If the numbers of
    elements is even, get the middle-nearest element

    :param l: elements
    :return: position of the middle element.
    """
    return floor(len(l) / 2)


def binary_search(l: list, item_to_search):
    """
    Call _do_binary_search on a sorted list with no item is cut (cut_item=0)

    :param l: elements
    :param item_to_search: item to search
    :return: position of item to search in list.
    """
    return _do_binary_search(l, item_to_search, 0)


def _do_binary_search(l, item_to_search, cut_item=0):
    """
    Do the binary search logic on a sorted list

    :param l: list of elements
    :param item_to_search: item to search
    :param cut_item: numbers of item be cut if item to search is in the right
    part of the list separated by the middle element.
    :return:
    """
    middle = get_middle_element(l)
    middle_value = l[middle]

    if item_to_search == middle_value:
        return middle + cut_item

    if item_to_search < middle_value:
        return _do_binary_search(l[:middle], item_to_search, cut_item)

    if item_to_search > middle_value:
        cut_item += len(l) - len(l[middle:])
        return _do_binary_search(l[middle:], item_to_search, cut_item)
