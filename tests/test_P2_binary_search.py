from practice.P2_binary_search import get_middle_element, binary_search


def test_get_middle():
    l = [1, 2, 3, 4, 5, 6]
    middle = get_middle_element(l)
    assert middle == 3
    assert l[middle] == 4

    l = [1, 2, 3]
    middle = get_middle_element(l)
    assert middle == 1
    assert l[middle] == 2


def test_binary_search():
    l = [1, 2, 3, 4, 5, 7]
    for i in l:
        assert binary_search(l, i) == l.index(i)

    l = [1, 2, 3, 4, 5, 7, 10]
    for i in l:
        assert binary_search(l, i) == l.index(i)

    l = [1, 2, 3, 4, 5, 7, 10, 11]
    for i in l:
        assert binary_search(l, i) == l.index(i)

    l = [1, 2, 3, 4]
    for i in l:
        assert binary_search(l, i) == l.index(i)