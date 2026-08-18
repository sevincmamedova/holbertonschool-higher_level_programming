#!/usr/bin/python3
"""Defines a text file appending function."""


def append_write(filename="", text=""):
    """Appends a string at the end of a UTF8 text file.

    The file is created if it does not exist.

    Args:
        filename: the name of the file to append to.
        text: the string to append to the file.

    Returns:
        The number of characters added.
    """
    with open(filename, "a", encoding="utf-8") as a_file:
        return a_file.write(text)
