#!/usr/bin/python3

"""Defines Fish, Bird, and FlyingFish classes to explore multiple inheritance."""

class Fish:
    """Class representing a fish."""

    def swim(self):
        """Prints the swimming behavior of the fish."""
        print("The fish is swimming")

    def habitat(self):
        """Prints the habitat of the fish."""
        print("The fish lives in water")

class Bird:
    """Class representing a bird."""

    def fly(self):
        """Prints the flying behavior of the bird."""
        print("The bird is flying")

    def habitat(self):
        """Prints the habitat of the bird."""
        print("The bird lives in the sky")

class FlyingFish(Fish, Bird):
    """Class representing a flying fish, inheriting from both Fish and Bird."""

    def swim(self):
        """Prints the swimming behavior of the flying fish."""
        print("The flying fish is swimming!")

    def fly(self):
        """Prints the flying behavior of the flying fish."""
        print("The flying fish is soaring!")

    def habitat(self):
        """Prints the habitat of the flying fish."""
        print("The flying fish lives both in water and the sky!")
