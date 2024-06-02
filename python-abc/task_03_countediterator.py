#!/usr/bin/python3

"""Defines a CountedIterator class to keep track of iterations."""

class CountedIterator:
    """Iterator class that counts the number of items iterated over."""

    def __init__(self, iterable):
        self.iterator = iter(iterable)
        self.count = 0

    def __next__(self):
        """Returns the next item and increments the count."""
        self.count += 1
        return next(self.iterator)

    def get_count(self):
        """Returns the count of iterated items."""
        return self.count
