#!/usr/bin/python3
"""Defines a rectangle."""


class Rectangle:
    """Represents a rectangle."""

    def __init__(self, width=0, height=0):
        """Initializes a new Rectangle.

        Args:
            width: the width of the new rectangle.
            height: the height of the new rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieves the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of the rectangle.

        Args:
            value: the new width of the rectangle.

        Raises:
            TypeError: if value is not an integer.
            ValueError: if value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieves the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of the rectangle.

        Args:
            value: the new height of the rectangle.

        Raises:
            TypeError: if value is not an integer.
            ValueError: if value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the area of the rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Returns the perimeter of the rectangle.

        The perimeter is 0 if the width or the height is equal to 0.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2

    def __str__(self):
        """Returns the rectangle drawn with the character #.

        An empty string is returned if the width or the height is 0.
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        rows = []
        for _ in range(self.__height):
            rows.append("#" * self.__width)
        return "\n".join(rows)

    def __repr__(self):
        """Returns a string able to recreate the rectangle with eval()."""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)
