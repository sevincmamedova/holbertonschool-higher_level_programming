#!/usr/bin/python3
"""Serializes and deserializes a dictionary to and from XML."""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """Serializes a dictionary to XML and saves it to a file.

    Every key becomes a child element of a <data> root element, and every
    value is stored as the text of that element.

    Args:
        dictionary: the Python dictionary to serialize.
        filename: the name of the output XML file.
    """
    root = ET.Element("data")
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)
    ET.ElementTree(root).write(filename, encoding="utf-8")


def deserialize_from_xml(filename):
    """Reads XML data from a file and rebuilds the dictionary.

    Every value is read back as a string, since XML does not carry types.

    Args:
        filename: the name of the input XML file.

    Returns:
        A Python dictionary with the deserialized XML data.
    """
    root = ET.parse(filename).getroot()
    return {child.tag: child.text for child in root}
