#!/usr/bin/python3
"""Defines a list subclass that can print itself sorted."""


class MyList(list):
    """Represents a list with a sorted printing method."""

    def print_sorted(self):
        """Prints the list in ascending order, without modifying it."""
        print(sorted(self))
