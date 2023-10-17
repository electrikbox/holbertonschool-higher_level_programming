#!/usr/bin/python3
"""class Student"""


class Student:
    """Student class"""

    def __init__(self, first_name, last_name, age):
        """init Student
        Args:
            first_name (str): Student first name
            last_name (str): Student last name
            age (int): Student age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """return Student dict
        Args:
            attrs (list, optional): Student attributs. Defaults to None.
        Returns:
            dict: Student dict
        """
        if attrs is None:
            return self.__dict__
        if all(isinstance(attr, str) for attr in attrs):
            return {k: v for k, v in self.__dict__.items() if k in attrs}
