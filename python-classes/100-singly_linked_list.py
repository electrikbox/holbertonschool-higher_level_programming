#!/usr/bin/python3
"""class Node that create a node for singly linked list"""


class Node:
    """class that create a new node"""

    def __init__(self, data, next_node=None):
        """init node

        Args:
            data (int): node value
            next_node (Node, optional): next node. Defaults to None.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if type(value) is not int:
            raise TypeError("data must be an integer")

        self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if value is None or isinstance(value, Node):
            self.__next_node = value
        else:
            raise TypeError("next_node must be None or a Node object")


class SinglyLinkedList:
    """class that create a new singly linked list"""

    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        """insert a new node

        Args:
            value (int): node value

        Raises:
            ValueError: if there's no value
            TypeError: if value is not an int
        """
        if value is None:
            raise ValueError("value can't be None")
        if type(value) is not int:
            raise TypeError("value must be an int")

        new_node = Node(value)

        if self.__head is None:
            self.__head = new_node
        else:
            if new_node.data <= self.__head.data:
                new_node.next_node = self.__head
                self.__head = new_node
            else:
                cur = self.__head
                while cur.next_node and new_node.data > cur.next_node.data:
                    cur = cur.next_node
                new_node.next_node = cur.next_node
                cur.next_node = new_node

    def __str__(self):
        elements = []
        current = self.__head
        while current:
            elements.append(str(current.data))
            current = current.next_node
        return "\n".join(elements)
