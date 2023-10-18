#!/usr/bin/python3
"""revert bool"""


class MyInt(int):
    """invert bool
    Args:
        int (int): mother class
    """
    def __eq__(self, num):
        return super().__ne__(num)

    def __ne__(self, num):
        return super().__eq__(num)
