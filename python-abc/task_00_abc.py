#!/usr/bin/python3

"""Defines abstract classes and subclasses for Animal, Dog, and Cat."""

from abc import ABC, abstractmethod

class Animal(ABC):
    """Abstract class representing an Animal."""

    @abstractmethod
    def sound(self):
        """Abstract method to be implemented by subclasses."""
        pass

class Dog(Animal):
    """Dog class inheriting from Animal."""

    def sound(self):
        """Returns the sound made by the dog."""
        return "Bark"

class Cat(Animal):
    """Cat class inheriting from Animal."""

    def sound(self):
        """Returns the sound made by the cat."""
        return "Meow"

