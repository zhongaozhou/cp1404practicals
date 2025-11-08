"""CP1404/CP5632 Practical - Guitar class.
Estimated time: 35 minutes
Actual time: 40 minites
"""

from datetime import datetime


class Guitar:
    """Represent a Guitar object."""

    def __init__(self, name="", year=0, cost=0):
        """Initialise a Guitar instance.

        name: string, name of the guitar
        year: integer, year the guitar was made
        cost: float, cost of the guitar
        """
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return a string of the Guitar."""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def __lt__(self, other):
        """Less than comparison for sorting by year."""
        return self.year < other.year

    def get_age(self):
        """Return how old the guitar is in years."""
        current_year = datetime.now().year
        return current_year - self.year

    def is_vintage(self):
        """Return True if the guitar is 50 or more years old, False if not."""
        return self.get_age() >= 50
