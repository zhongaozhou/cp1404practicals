"""CP1404/CP5632 Practical - Testing the Guitar class.
Estimated time: 25 minutes
Actual time: 20 minutes
"""

from prac_06.guitar import Guitar


def main():
    """Test the Guitar class methods."""
    # Create test guitars
    guitar1 = Guitar("Gibson L-5 CES", 1922, 16035.40)
    guitar2 = Guitar("Another Guitar", 2013, 100.00)

    print(guitar1)
    print(guitar2)

    # Test get_age() method
    print(f"Gibson L-5 CES get_age() - Expected {2025 - 1922}. Got {guitar1.get_age()}")
    print(f"Another Guitar get_age() - Expected {2025 - 2013}. Got {guitar2.get_age()}")

    # Test is_vintage() method
    print(f"Gibson L-5 CES is_vintage() - Expected True. Got {guitar1.is_vintage()}")
    print(f"Another Guitar is_vintage() - Expected False. Got {guitar2.is_vintage()}")


main()
