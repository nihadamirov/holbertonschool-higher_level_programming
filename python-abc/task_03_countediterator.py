#!/usr/bin/python3

"""Defines a CountedIterator class that tracks iteration count."""

class CountedIterator:
    """Iterator that counts the number of items iterated over."""

    def __init__(self, iterable):
        self.iterator = iter(iterable)
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        try:
            item = next(self.iterator)
            self.count += 1
            return item
        except StopIteration:
            raise StopIteration

    def get_count(self):
        """Returns the count of items iterated over."""
        return self.count
