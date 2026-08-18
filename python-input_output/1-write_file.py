#!/usr/bin/python3
"""Defines a text file writing function."""


def write_file(filename="", text=""):
    """Writes a string to a UTF8 text file, overwriting its content.

    The file is created if it does not exist.

    Args:
        filename: the name of the file to write to.
        text: the string to write to the file.

    Returns:
        The number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as a_file:
        return a_file.write(text)
