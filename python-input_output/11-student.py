#!/usr/bin/python3
"""Defines a student."""


class Student:
    """Represents a student."""

    def __init__(self, first_name, last_name, age):
        """Initializes a new Student.

        Args:
            first_name: the first name of the student.
            last_name: the last name of the student.
            age: the age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns the dictionary representation of the Student.

        Args:
            attrs: a list of attribute names to retrieve. Every attribute is
                retrieved when it is not a list of strings.
        """
        if (type(attrs) is list and
                all(type(name) is str for name in attrs)):
            return {key: value for key, value in self.__dict__.items()
                    if key in attrs}
        return self.__dict__.copy()

    def reload_from_json(self, json):
        """Replaces every attribute of the Student from a dictionary.

        Args:
            json: a dictionary whose keys are public attribute names and
                whose values are the new attribute values.
        """
        for key, value in json.items():
            setattr(self, key, value)
