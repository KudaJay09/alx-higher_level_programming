#!/usr/bin/python3
"""Define a json file reading function"""
import json


def load_from_json_file(filename):
    """Make Python object from a json file."""
    with open(filename) as f:
        return json.load(f)
