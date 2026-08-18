#!/usr/bin/python3
def element_at(my_list, idx):
    """Retrieves the element of a list at a given index.

    Returns None if the index is negative or out of range.
    """
    if idx < 0 or idx >= len(my_list):
        return None
    return my_list[idx]
