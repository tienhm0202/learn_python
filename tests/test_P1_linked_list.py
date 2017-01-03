from practice.P1_linked_list import LinkedList, Node


def test_add_at_last():
    a = LinkedList()

    n0 = Node(0)
    a.add_at_last(n0)
    assert {0: 0} == a.print_all()
    assert a.size == 1
    assert a.first_node == a.last_node

    n1 = Node(1)
    a.add_at_last(n1)
    assert {0: 0, 1: 1} == a.print_all()
    assert a.size == 2
    assert a.first_node.next == a.last_node
    assert a.first_node.value == 0
    assert a.last_node.prev == a.first_node
    assert a.last_node.value == 1

    n2 = Node(2)
    a.add_at_last(n2)
    assert {0: 0, 1: 1, 2: 2} == a.print_all()
    assert a.size == 3
    assert a.first_node.next.next == a.last_node
    assert a.last_node.prev.prev == a.first_node


def test_add_at_first():
    a = LinkedList()

    n0 = Node(2)
    a.add_at_first(n0)
    assert {0: 2} == a.print_all()
    assert a.size == 1

    n1 = Node(1)
    a.add_at_first(n1)
    assert {0: 1, 1: 2} == a.print_all()
    assert a.size == 2

    n2 = Node(0)
    a.add_at_first(n2)
    assert {0: 0, 1: 1, 2: 2} == a.print_all()
    assert a.size == 3


def test_remove_last():
    a = LinkedList()
    n0 = Node(0)
    a.add_at_last(n0)
    n1 = Node(1)
    a.add_at_last(n1)
    n2 = Node(2)
    a.add_at_last(n2)

    assert {0: 0, 1: 1, 2: 2} == a.print_all()
    assert a.size == 3

    a.remove_last()
    assert {0: 0, 1: 1} == a.print_all()
    assert a.size == 2

    a.remove_last()
    assert {0: 0} == a.print_all()
    assert a.size == 1
    assert a.first_node == a.last_node

    a.remove_last()
    assert {} == a.print_all()
    assert a.size == 0
    assert a.first_node is None
    assert a.last_node is None

    a.remove_last()
    assert {} == a.print_all()
    assert a.size == 0


def test_remove_first():
    a = LinkedList()
    n0 = Node(0)
    a.add_at_last(n0)
    n1 = Node(1)
    a.add_at_last(n1)
    n2 = Node(2)
    a.add_at_last(n2)

    assert {0: 0, 1: 1, 2: 2} == a.print_all()
    assert a.size == 3

    a.remove_first()
    assert {0: 1, 1: 2} == a.print_all()
    assert a.size == 2

    a.remove_first()
    assert {0: 2} == a.print_all()
    assert a.size == 1
    assert a.first_node == a.last_node

    a.remove_first()
    assert {} == a.print_all()
    assert a.size == 0
    assert a.first_node is None
    assert a.last_node is None

    a.remove_first()
    assert {} == a.print_all()
    assert a.size == 0
