#!/usr/bin/python3
"""Defines a class membership checking function."""


def is_same_class(obj, a_class):
    """Returns True if obj is exactly an instance of a_class, else False.

    Args:
        obj: the object to check.
        a_class: the class the object has to be an exact instance of.
    """
    return type(obj) is a_class
