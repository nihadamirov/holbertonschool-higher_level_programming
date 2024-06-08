#!/usr/bin/env python3
import json

def serialize_and_save_to_file(data, filename):
    """Serialize a dictionary and save it to a JSON file.

    Args:
        data (dict): The dictionary to serialize.
        filename (str): The name of the JSON file to save the data to.
    """
    with open(filename, 'w') as file:
        json.dump(data, file)

def load_and_deserialize(filename):
    """Load and deserialize data from a JSON file.

    Args:
        filename (str): The name of the JSON file to load the data from.

    Returns:
        dict: The deserialized data.
    """
    with open(filename, 'r') as file:
        return json.load(file)

