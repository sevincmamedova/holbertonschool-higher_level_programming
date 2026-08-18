#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """Replaces an element of a list at a specific position, in a copy.

    The original list is never modified, and a copy of it is returned
    unchanged if the index is negative or out of range.
    """
    new_list = my_list[:]
    if idx < 0 or idx >= len(my_list):
        return new_list
    new_list[idx] = element
    return new_list
