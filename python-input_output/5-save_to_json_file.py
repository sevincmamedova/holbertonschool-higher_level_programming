#!/usr/bin/python3
"""Defines a JSON file writing function."""
import json


def save_to_json_file(my_obj, filename):
    """Writes an object to a text file, using a JSON representation.

    Args:
        my_obj: the object to serialize.
        filename: the name of the file to write to.
    """
    with open(filename, "w", encoding="utf-8") as a_file:
        json.dump(my_obj, a_file)
