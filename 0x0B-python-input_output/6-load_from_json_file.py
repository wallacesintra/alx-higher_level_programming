#!/usr/bin/python3
"""JSON file-reading function"""
import json


def load_from_json_file(filename):
    """
    a function that creates an Object from a JSON file
    """
    with open(filename) as myFile:
        return json.load(myFile)
