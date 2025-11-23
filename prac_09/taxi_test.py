"""
CP1404/CP5632 Practical - Testing the Taxi class
"""

from prac_09.taxi import Taxi


def main():
    """Test the Taxi class."""
    my_taxi = Taxi("Prius 1", 100)

    # Drive the taxi 40 km
    distance_driven = my_taxi.drive(40)
    print(f"Actually drove {distance_driven}km")

    # Print the taxi's details and the current fare
    print("\nTaxi details after first trip:")
    print(my_taxi)
    print(f"Current fare: ${my_taxi.get_fare():.2f}")

    # Restart the meter (start a new fare)
    print("\nRestarting meter...")
    my_taxi.start_fare()

    # Drive the car 100 km
    print("Driving taxi 100km...")
    distance_driven = my_taxi.drive(100)
    print(f"Actually drove {distance_driven}km")

    # Print the details and the current fare
    print("\nTaxi details after second trip:")
    print(my_taxi)
    print(f"Current fare: ${my_taxi.get_fare():.2f}")


if __name__ == '__main__':
    main()
