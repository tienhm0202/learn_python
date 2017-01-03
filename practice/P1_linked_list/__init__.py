class Node(object):
    """A node will be use as an element in linked list"""
    def __init__(self, value, _next=None, _prev=None):
        self.value = value
        self.next = _next
        self.prev = _prev


class LinkedList(object):
    def __init__(self):
        self.first_node = None
        self.last_node = None
        self.size = 0

    def add_at_last(self, node):
        """
        Add a node at the end of list
        :param node: Node
        """
        if self.is_empty():
            self.first_node = self.last_node = node
        else:
            self.last_node.next = node
            node.prev = self.last_node
            self.last_node = node

        self.size += 1

    def remove_last(self):
        """Remove last node"""
        if self.is_empty():
            return

        if self.size > 1:
            self.last_node = self.last_node.prev
            self.last_node.next = None
        else:
            self.first_node = None
            self.last_node = None

        self.size -= 1

    def add_at_first(self, node):
        """
        Add a node at the beginning of list
        :param node: Node
        """
        if self.first_node is None:
            self.first_node = self.last_node = node
        else:
            self.first_node.prev = node
            node.next = self.first_node
            self.first_node = node

        self.size += 1

    def remove_first(self):
        """Remove first node"""
        if self.is_empty():
            return

        if self.size > 1:
            self.first_node = self.first_node.next
            self.first_node.prev = None
        else:
            self.first_node = None
            self.last_node = None
        self.size -= 1

    def is_empty(self):
        """
        Check if linked list is empty or not
        :return: bool
        """
        return self.size == 0

    def print_all(self):
        if self.first_node is None:
            return {}

        d = {0: self.first_node.value}
        i = 0

        current = self.first_node
        while current.next is not None:
            current = current.next
            i += 1
            d[i] = current.value

        return d
