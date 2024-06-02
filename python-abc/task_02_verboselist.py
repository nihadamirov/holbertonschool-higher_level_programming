#!/usr/bin/python3

"""Defines a VerboseList class that extends the built-in list class."""

class VerboseList(list):
    """Custom list class that prints notifications on certain actions."""

    def append(self, item):
        """Appends an item to the list and prints a notification."""
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, items):
        """Extends the list with multiple items and prints a notification."""
        super().extend(items)
        print(f"Extended the list with [{len(items)}] items.")

    def remove(self, item):
        """Removes an item from the list and prints a notification."""
        print(f"Removed [{item}] from the list.")
        super().remove(item)

    def pop(self, index=-1):
        """Pops an item from the list and prints a notification."""
        item = self[index]
        print(f"Popped [{item}] from the list.")
        return super().pop(index)
