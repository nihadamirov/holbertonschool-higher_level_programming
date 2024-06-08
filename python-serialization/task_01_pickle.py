#!/usr/bin/env python3
import pickle

class CustomObject:
    """A custom object with name, age, and student status."""

    def __init__(self, name, age, is_student):
        """Initialize a new CustomObject.

        Args:
            name (str): The name of the person.
            age (int): The age of the person.
            is_student (bool): Whether the person is a student.
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Display the attributes of the CustomObject."""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """Serialize the object to a file using pickle.

        Args:
            filename (str): The name of the file to write the object to.
        """
        try:
            with open(filename, 'wb') as file:
                pickle.dump(self, file)
        except (FileNotFoundError, pickle.PickleError) as e:
            print(f"Serialization error: {e}")

    @classmethod
    def deserialize(cls, filename):
        """Deserialize an object from a file using pickle.

        Args:
            filename (str): The name of the file to read the object from.

        Returns:
            CustomObject: The deserialized object, or None if deserialization fails.
        """
        try:
            with open(filename, 'rb') as file:
                return pickle.load(file)
        except (FileNotFoundError, pickle.PickleError) as e:
            print(f"Deserialization error: {e}")
            return None
