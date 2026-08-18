#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    """Returns a list of booleans telling which integers are multiples of 2.

    The new list has the same size as the original one.
    """
    return [number % 2 == 0 for number in my_list]
