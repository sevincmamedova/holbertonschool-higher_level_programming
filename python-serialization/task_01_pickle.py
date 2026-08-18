#!/usr/bin/python3
"""Serializes and deserializes a custom object with the pickle module."""
import pickle


class CustomObject:
    """Represents a custom object that can be pickled."""

    def __init__(self, name, age, is_student):
        """Initializes a new CustomObject.

        Args:
            name: the name of the object.
            age: the age of the object.
            is_student: whether the object is a student.
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Prints the attributes of the object."""
        print("Name: {}".format(self.name))
        print("Age: {}".format(self.age))
        print("Is Student: {}".format(self.is_student))

    def serialize(self, filename):
        """Serializes the current instance and saves it to a file.

        Args:
            filename: the name of the file to write to.

        Returns:
            None if the object could not be serialized.
        """
        try:
            with open(filename, "wb") as a_file:
                pickle.dump(self, a_file)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        """Loads and returns a CustomObject instance from a file.

        Args:
            filename: the name of the file to read from.

        Returns:
            The deserialized instance, or None if the file does not exist
            or is malformed.
        """
        try:
            with open(filename, "rb") as a_file:
                return pickle.load(a_file)
        except Exception:
            return None
