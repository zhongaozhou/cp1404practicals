"""
CP1404/CP5632 Practical
SilverServiceTaxi class
"""
from prac_09.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Specialised version of Taxi with fanciness and flagfall."""
    flagfall = 4.50  # Class variable

    def __init__(self, name, fuel, fanciness):
        """
        Initialise a SilverServiceTaxi instance, based on parent class Taxi.

        fanciness: float that multiplies the base price_per_km
        """
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km = Taxi.price_per_km * fanciness

    def get_fare(self):
        """Return the price for the taxi trip including flagfall."""
        # Use parent's get_fare() method (which includes rounding)
        base_fare = super().get_fare()
        return base_fare + self.flagfall

    def __str__(self):
        """Return a string representation including fanciness and flagfall."""
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}"
