"""
CP1404/CP5632 Practical - Testing the UnreliableCar class
"""

from prac_09.unreliable_car import UnreliableCar


def single_drive():
    """Test a single drive attempt to demonstrate the concept."""
    print("Testing Single Drive")
    # Create a car with 50% reliability
    unreliable_car = UnreliableCar("Old Clunker", 100, 50.0)
    print(f"Before drive: {unreliable_car}")

    # Attempt to drive 20km
    distance_driven = unreliable_car.drive(20)
    print(f"Attempted to drive 20km, actually drove: {distance_driven}km")
    print(f"After drive: {unreliable_car}")
    print()


def multiple_drives():
    """Test multiple drive attempts to observe reliability pattern."""
    print("Testing Multiple Drives (Statistics)")

    # Test with high reliability car (90%)
    reliable_car = UnreliableCar("Reliable Runner", 200, 90.0)
    successful_drives = 0
    total_attempts = 100

    print(f"Testing {reliable_car.name} with {reliable_car.reliability}% reliability")
    print(f"Performing {total_attempts} drive attempts of 10km each...")

    for i in range(total_attempts):
        distance_driven = reliable_car.drive(10)
        if distance_driven > 0:
            successful_drives += 1

    success_rate = (successful_drives / total_attempts) * 100
    print(f"Successful drives: {successful_drives}/{total_attempts} ({success_rate:.1f}%)")
    print(f"Final state: {reliable_car}")
    print()


def low_reliability():
    """Test with a low reliability car."""
    print("Testing Low Reliability Car")

    unreliable_car = UnreliableCar("Barely Working", 100, 30.0)
    successful_drives = 0
    total_attempts = 50

    print(f"Testing {unreliable_car.name} with {unreliable_car.reliability}% reliability")
    print(f"Performing {total_attempts} drive attempts of 5km each...")

    for i in range(total_attempts):
        distance_driven = unreliable_car.drive(5)
        if distance_driven > 0:
            successful_drives += 1

    success_rate = (successful_drives / total_attempts) * 100
    print(f"Successful drives: {successful_drives}/{total_attempts} ({success_rate:.1f}%)")
    print(f"Final state: {unreliable_car}")
    print()


def main():
    """Run all tests for UnreliableCar."""
    single_drive()
    multiple_drives()
    low_reliability()


if __name__ == '__main__':
    main()
