#!/usr/bin/python3

"""Defines SwimMixin and FlyMixin classes and a Dragon class inheriting from both."""

class SwimMixin:
    """Mixin class that provides swimming ability."""

    def swim(self):
        """Prints the swimming behavior of the creature."""
        print("The creature swims!")

class FlyMixin:
    """Mixin class that provides flying ability."""

    def fly(self):
        """Prints the flying behavior of the creature."""
        print("The creature flies!")

class Dragon(SwimMixin, FlyMixin):
    """Class representing a dragon, inheriting from SwimMixin and FlyMixin."""

    def roar(self):
        """Prints the roaring behavior of the dragon."""
        print("The dragon roars!")
