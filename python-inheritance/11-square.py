#!/usr/bin/python3
"""Defines a square based on a rectangle."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represents a square."""

    def __init__(self, size):
        """Initializes a new Square.

        Args:
            size: the size of the new square.

        Raises:
            TypeError: if size is not an integer.
            ValueError: if size is less than or equal to 0.
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Returns the area of the square."""
        return self.__size * self.__size

    def __str__(self):
        """Returns the square description: [Square] <width>/<height>."""
        return "[Square] {}/{}".format(self.__size, self.__size)
