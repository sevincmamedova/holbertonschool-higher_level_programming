#!/usr/bin/python3
"""Defines a base geometry."""


class BaseGeometry:
    """Represents a base geometry."""

    def area(self):
        """Raises an Exception, as the area is not implemented.

        Raises:
            Exception: always, with the message area() is not implemented.
        """
        raise Exception("area() is not implemented")
