#!/usr/bin/python3
"""Defines a JSON file-writing function."""
import json


def load_from_json_file(filename):
    """creates an Object from a 'JSON file' """
    with open(filename, mode="w", encoding="utf-8") as f:
        json.load(f)
