#!/usr/bin/python3
"""Defines a class serialization function."""


def class_to_json(obj):
    """Returns the dictionary description of an object for JSON serialization.

    Only the attributes set on the instance are described, using simple data
    structures: list, dictionary, string, integer and boolean.

    Args:
        obj: the instance to describe.
    """
    return obj.__dict__.copy()
