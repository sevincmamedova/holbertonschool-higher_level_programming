#!/usr/bin/python3
"""Defines a JSON deserialization function."""
import json


def from_json_string(my_str):
    """Returns the Python data structure represented by a JSON string.

    Args:
        my_str: the JSON string to deserialize.
    """
    return json.loads(my_str)
