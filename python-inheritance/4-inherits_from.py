#!/usr/bin/python3
"""Defines a subclass checking function."""


def inherits_from(obj, a_class):
    """Returns True if obj is an instance of a strict subclass of a_class.

    An object that is exactly an instance of a_class returns False.

    Args:
        obj: the object to check.
        a_class: the class the object has to inherit from.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
