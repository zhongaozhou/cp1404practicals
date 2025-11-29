"""
CP1404/CP5632 Practical
UnreliableCar class - derived from Car with reliability feature
"""
from prac_06.car import Car
import random


class UnreliableCar(Car):
    """Specialised version of Car that may not always drive."""

    def __init__(self, name, fuel, reliability):
        """
        Initialise an UnreliableCar instance, based on parent class Car.

        reliability: float between 0 and 100 representing percentage chance to drive
        """
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """
        Drive the car only if it passes reliability check.

        Generate random number and only drive if it's less than reliability.
        Returns the distance driven (could be 0 if unreliable).
        """
        random_number = random.uniform(0, 100)
        if random_number < self.reliability:
            # Car is reliable this time
            return super().drive(distance)
        else:
            # Car is unreliable
            return 0

    def __str__(self):
        """Return a string representation including reliability."""
        return f"{super().__str__()}, reliability={self.reliability}%"