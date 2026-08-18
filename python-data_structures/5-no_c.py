#!/usr/bin/python3
def no_c(my_string):
    """Returns a copy of a string with all c and C characters removed."""
    new_string = ""
    for c in my_string:
        if c != "c" and c != "C":
            new_string += c
    return new_string
