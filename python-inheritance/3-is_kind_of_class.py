#!/usr/bin/python3
"""Defines a class inheritance checking function."""


def is_kind_of_class(obj, a_class):
    """Returns True if obj is an instance of a_class or of a subclass of it.

    Args:
        obj: the object to check.
        a_class: the class the object has to come from.
    """
    return isinstance(obj, a_class)
