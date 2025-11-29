"""
CP1404/CP5632 Practical - Taxi Simulator
Program that demonstrates polymorphism with Taxi and SilverServiceTaxi classes
"""

from prac_09.taxi import Taxi
from prac_09.silver_service_taxi import SilverServiceTaxi


def main():
    """Main taxi simulator program."""
    print("Let's drive!")

    # Create a list of taxis
    taxis = [
        Taxi("Prius", 100),
        SilverServiceTaxi("Limo", 100, 2),
        SilverServiceTaxi("Hummer", 200, 4)
    ]

    current_taxi = None
    total_bill = 0.0

    while True:
        print(f"Bill to date: ${total_bill:.2f}")
        choice = input("q)uit, c)hoose taxi, d)rive\n>>> ").lower()

        if choice == 'q':
            break
        elif choice == 'c':
            current_taxi = choose_taxi(taxis)
        elif choice == 'd':
            if current_taxi is None:
                print("You need to choose a taxi before you can drive")
            else:
                cost = drive_taxi(current_taxi)
                total_bill += cost
                print(f"Your {current_taxi.name} trip cost you ${cost:.2f}")
        else:
            print("Invalid option")

    # Final output
    print(f"\nTotal trip cost: ${total_bill:.2f}")
    print("Taxis are now:")
    display_taxis(taxis)


def choose_taxi(taxis):
    """Let user choose a taxi from available taxis."""
    print("Taxis available: ")
    display_taxis(taxis)

    try:
        choice = int(input("Choose taxi: "))
        if 0 <= choice < len(taxis):
            return taxis[choice]
        else:
            print("Invalid taxi choice")
            return None
    except ValueError:
        print("Invalid input")
        return None


def drive_taxi(taxi):
    """Drive the chosen taxi and return the cost."""
    try:
        distance = float(input("Drive how far? "))
    except ValueError:
        print("Invalid distance")
        return 0.0

    # Start a new fare
    taxi.start_fare()

    # Drive the taxi
    distance_driven = taxi.drive(distance)

    # Get the fare
    cost = taxi.get_fare()

    return cost


def display_taxis(taxis):
    """Display all available taxis with their numbers."""
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


if __name__ == '__main__':
    main()
