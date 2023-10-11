#!/usr/bin/python3

"""class Rectangle that defines a rectangle"""
class Square:
    """ Square class that define a square with is size"""

    def __init__(self, size=0, position=(0, 0)):
        """Instantiate a square with optional size

        Args:
            size (int, optional): Size of the square. Defaults to 0.
            position (tuple, optional): Square position. Defaults to (0, 0).
        """
        self.size = size
        self.position = position

    @property
    def size(self):  # get the square size
        return self.__size

    @size.setter
    def size(self, value):  # set the square size

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    @property
    def position(self):  # get the square position
        return self.__position

    @position.setter
    def position(self, value):  # set the square size

        if (
            not isinstance(value, tuple)
            or len(value) != 2 or
            not isinstance(value[0], int)
            or not isinstance(value[1], int)
            or value[0] < 0 or value[1] < 0
        ):
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value

    def area(self):
        """Return the current square area."""
        return self.__size ** 2

    def my_print(self):
        """Print the square with the # character."""
        if self.__size == 0:
            print("")
            return

        [print("") for i in range(self.__position[1])]
        for i in range(self.__size):
            [print(" ", end="") for j in range(self.__position[0])]
            [print("#", end="") for k in range(self.__size)]
            print("")


class Rectangle:
    """class Rectangle that defines a rectangle."""

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """initializes the rectangle.

        Args:
            width (int, optional): rectangle width. Defaults to 0.
            height (int, optional): rectangle height. Defaults to 0.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """width getter.

        Raises:
            TypeError: width must be an integer
            ValueError: width must be >= 0
        """
        return self.__width

    @width.setter
    def width(self, value):
        """width setter.

        Args:
            value (int): width value.
        Raises:
            TypeError: width must be an integer
            ValueError: width must be >= 0
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """height getter.

        Raises:
            TypeError: height must be an integer
            ValueError: height must be >= 0
        """
        return self.__height

    @height.setter
    def height(self, value):
        """height setter.

        Args:
            value (int): height value.
        Raises:
            TypeError: height must be an integer
            ValueError: height must be >= 0
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the area of the rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Returns the perimeter of the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2

    def __str__(self):
        """print rectangle"""
        if self.__height == 0 or self.__width == 0:
            return ""
        else:
            rect_str = ""
            for i in range(self.__height):
                rect_str += str(str(self.print_symbol)) * self.__width + "\n"
            return rect_str[:-1]

    def __repr__(self):
        """print representation of a rectangle"""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """print message when deleting a rectangle"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
        return

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """get the bigger rectangle.

        Args:
            rect_1 (Rectangle): rectangle 1.
            rect_2 (Rectangle): rectangle 2.

        Raises:
            TypeError: if rect_& or rect_2 is not Rectangle type

        Returns:
            Rectangle: bigger rectangle.
        """
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """_summary_

        Args:
            size (int, optional): size of the square. Defaults to 0.

        Returns:
            Rectangle: rectangle with same width and height
        """
        return cls(size, size)
