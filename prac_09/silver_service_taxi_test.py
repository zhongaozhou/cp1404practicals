"""
CP1404/CP5632 Practical - Testing the SilverServiceTaxi class
"""

from prac_09.silver_service_taxi import SilverServiceTaxi


def test_silver_service_taxi_creation():
    """Test creating SilverServiceTaxi objects."""
    print("\nTesting SilverServiceTaxi Creation")

    # Test with different fanciness levels
    hummer = SilverServiceTaxi("Hummer", 200, 4)
    limo = SilverServiceTaxi("Limo", 100, 2)

    print("Hummer details:", hummer)
    print("Limo details:", limo)
    print()


def test_fare_calculation():
    """Test fare calculation with assertions."""
    print("\nTesting Fare Calculation")

    # Test case: 18km trip with fanciness 2
    taxi = SilverServiceTaxi("Test Taxi", 100, 2)
    taxi.drive(18)
    fare = taxi.get_fare()

    print(f"Taxi: {taxi}")
    print(f"Fare for 18km trip: ${fare:.2f}")

    # Expected calculation: (1.23 * 2 * 18) + 4.50 = 44.28 + 4.50 = 48.78
    # But with rounding to nearest 10c: 48.80
    expected_fare = 48.80
    assert abs(fare - expected_fare) < 0.01, f"Expected ${expected_fare:.2f}, got ${fare:.2f}"
    print(f"Fare calculation correct: ${fare:.2f}")
    print()


def test_different_fanciness():
    """Test different fanciness levels."""
    print("\nTesting Different Fanciness Levels")

    test_cases = [
        ("Budget", 1.0, 10, 16.80),  # (1.23 * 1 * 10) + 4.50 = 12.30 + 4.50 = 16.80
        ("Standard", 2.0, 10, 29.10),  # (1.23 * 2 * 10) + 4.50 = 24.60 + 4.50 = 29.10
        ("Luxury", 4.0, 10, 53.70),  # (1.23 * 4 * 10) + 4.50 = 49.20 + 4.50 = 53.70
    ]

    for name, fanciness, distance, expected_fare in test_cases:
        taxi = SilverServiceTaxi(name, 100, fanciness)
        taxi.drive(distance)
        fare = taxi.get_fare()

        assert abs(fare - expected_fare) < 0.01, f"{name} fare incorrect"
        print(f"{name} (fanciness {fanciness}): ${fare:.2f}")

    print()


def main():
    """Run all SilverServiceTaxi tests."""
    test_silver_service_taxi_creation()
    test_fare_calculation()
    test_different_fanciness()


if __name__ == '__main__':
    main()
