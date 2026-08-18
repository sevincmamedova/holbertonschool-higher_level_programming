#!/usr/bin/python3
"""Serializes and deserializes a Python dictionary to and from a JSON file."""
import json


def serialize_and_save_to_file(data, filename):
    """Serializes a dictionary to JSON and saves it to a file.

    An existing file is replaced.

    Args:
        data: the Python dictionary to serialize.
        filename: the name of the output JSON file.
    """
    with open(filename, "w", encoding="utf-8") as a_file:
        json.dump(data, a_file)


def load_and_deserialize(filename):
    """Loads a JSON file and deserializes it into a Python dictionary.

    Args:
        filename: the name of the input JSON file.

    Returns:
        A Python dictionary with the deserialized JSON data.
    """
    with open(filename, encoding="utf-8") as a_file:
        return json.load(a_file)
