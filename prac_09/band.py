"""
CP1404/CP5632 Practical
Band class using association with Musician objects
"""


class Band:
    """Band class representing a band with multiple musicians."""

    def __init__(self, name=""):
        """Construct a Band with a name and empty musicians collection."""
        self.name = name
        self.musicians = []

    def __str__(self):
        """Return a string representation of the Band."""
        musician_strings = [str(musician) for musician in self.musicians]
        return f"{self.name} ({', '.join(musician_strings)})"

    def __repr__(self):
        """Return a string representation of the Band, showing the variables."""
        return str(vars(self))

    def add(self, musician):
        """Add a musician to the band."""
        self.musicians.append(musician)

    def play(self):
        """Return a string showing each musician playing their instrument."""
        play_results = []
        for musician in self.musicians:
            play_results.append(musician.play())
        return "\n".join(play_results)
