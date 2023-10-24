#!/usr/bin/python3
"""
represent a base class that will help for future
rectangle and square classes
"""

import json
import os
import turtle


class Base:
    """Base class"""

    # INIT ---------------------------------------------------------------

    __nb_objects = 0

    def __init__(self, id=None):
        """initialisation
        Args:
            id (int, optional): object identifier. Defaults to None.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    # JSON <-> STRING ----------------------------------------------------

    @staticmethod
    def from_json_string(json_string):
        """Convert a JSON string to a list of dictionaries.
        Args:
            json_string (str): A JSON string to be converted.
        Returns:
            list: A list of dictionaries parsed from the JSON string.
        """
        if not json_string:
            return []
        return json.loads(json_string)

    @staticmethod
    def to_json_string(list_dictionaries):
        """Convert a list of dictionaries to a JSON string.
        Args:
            list_dictionaries (list): A list of dictionaries to be converted.
        Returns:
            str: A JSON representation of the list of dictionaries.
        """
        if list_dictionaries is None or list_dictionaries == "[]":
            return "[]"
        return json.dumps(list_dictionaries)

    # LOAD AND SAVE (FILE) -----------------------------------------------

    @classmethod
    def save_to_file(cls, list_objs):
        """Save a list of objects to a JSON file.
        Args:
            cls (class): The class of the objects in the list.
            list_objs (list): A list of objects to be saved to a JSON file.
        """
        if list_objs is None:
            list_objs = []

        filename = f"{cls.__name__}.json"
        data = [obj.to_dictionary() for obj in list_objs]
        json_str = Base.to_json_string(data)

        with open(filename, 'w') as file:
            file.write(json_str)

    @classmethod
    def load_from_file(cls):
        """Load a list of instances from a JSON file.
        Args:
            cls (class): The class of the instances to be loaded from the file.
        Returns:
            list: A list of instances parsed from the JSON file.
        """
        file_name = f"{cls.__name__}.json"
        if os.path.exists(file_name) is False:
            return []
        with open(file_name, "r") as file:
            data = file.read()
            instance_list = cls.from_json_string(data)
            return [cls.create(**dictionnary) for dictionnary in instance_list]

    # CREATE -------------------------------------------------------------

    @classmethod
    def create(cls, **dictionary):
        """Create a new instance based on a dictionary of attributes.
        Args:
            cls (class): The class of the instance to be created.
            dictionary (dict): A dictionary of attributes for the new instance.
        Returns:
            object: Instance of the class with attributes from the dict.
        """
        if cls.__name__ == "Rectangle":
            new = cls(10, 10)
        else:
            new = cls(10)
        new.update(**dictionary)
        return new

    # DRAW ---------------------------------------------------------------

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draws all the Rectangles and Squares.
        Args:
            list_rectangles (list): a list of rectangle.
            list_squares (list): a list of square.
        """
        draw = turtle.Turtle()
        draw.screen.bgcolor('#93dad3')
        draw.shape('arrow')
        draw.color('#3b736e')
        draw.width(2)
        draw.penup()
        draw.goto(-300, 400)

        for rect in list_rectangles:
            Base.setup_draw(draw, rect)
            for _ in range(2):
                draw.forward(rect.width)
                draw.left(90)
                draw.forward(rect.height)
                draw.left(90)
            draw.end_fill()
            draw.penup()

        for square in list_squares:
            Base.setup_draw(draw, square)
            for _ in range(4):
                draw.forward(square.width)
                draw.left(90)
            draw.end_fill()
            draw.penup()

        draw.goto(-400, 400)
        draw.screen.exitonclick()

    @staticmethod
    def setup_draw(instance, obj):
        instance.goto(instance.xcor(), instance.ycor() - (obj.height + 10))
        instance.penup()
        instance.pendown()
        instance.begin_fill()
