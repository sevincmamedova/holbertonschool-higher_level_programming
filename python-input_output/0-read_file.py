#!/usr/bin/python3
"""Defines a text file reading function."""


def read_file(filename=""):
    """Reads a UTF8 text file and prints its content to stdout.

    Args:
        filename: the name of the file to read.
    """
    with open(filename, encoding="utf-8") as a_file:
        print(a_file.read(), end="")
