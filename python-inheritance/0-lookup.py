#!/usr/bin/python3
"""Defines a lookup function."""


def lookup(obj):
    """Returns the list of available attributes and methods of an object.

    Args:
        obj: the object to inspect.
    """
    return dir(obj)
