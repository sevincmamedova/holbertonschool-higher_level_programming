#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    """Adds the first 2 integers of two tuples, element by element.

    Missing integers are replaced by the value 0.
    """
    a = tuple_a + (0, 0)
    b = tuple_b + (0, 0)
    return (a[0] + b[0], a[1] + b[1])
