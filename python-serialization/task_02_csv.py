#!/usr/bin/python3
"""Converts CSV data to JSON format."""
import csv
import json


def convert_csv_to_json(csv_filename):
    """Reads a CSV file and writes its data to data.json.

    Each row of the CSV file becomes a dictionary keyed by the header row.

    Args:
        csv_filename: the name of the CSV file to read.

    Returns:
        True if the conversion succeeded, False otherwise.
    """
    try:
        with open(csv_filename, encoding="utf-8") as csv_file:
            data = list(csv.DictReader(csv_file))
    except Exception:
        return False

    try:
        with open("data.json", "w", encoding="utf-8") as json_file:
            json.dump(data, json_file)
    except Exception:
        return False

    return True
