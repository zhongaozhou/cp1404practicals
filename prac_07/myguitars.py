"""
CP1404/CP5632 Practical - My Guitars program
Estimated time: 35 minutes
Actual time:42 minutes
"""

from guitar import Guitar


def main():
    """Main program to manage guitar collection."""
    guitars = load_guitars()

    print("All guitars:")
    display_guitars(guitars)

    # Sort guitars by year
    guitars.sort()
    print("\nGuitars sorted by year (oldest to newest):")
    display_guitars(guitars)

    # Add new guitars
    add_new_guitars(guitars)

    # Save all guitars back to file
    save_guitars(guitars)
    print(f"\nSaved {len(guitars)} guitars to file.")


def load_guitars():
    """Load guitars from guitars.csv file."""
    guitars = []
    try:
        with open('guitars.csv', 'r') as file:
            for line in file:
                parts = line.strip().split(',')
                if len(parts) == 3:
                    name = parts[0]
                    year = int(parts[1])
                    cost = float(parts[2])
                    guitar = Guitar(name, year, cost)
                    guitars.append(guitar)
        print(f"Loaded {len(guitars)} guitars from file.")
    except FileNotFoundError:
        print("No existing guitar file found. Starting with empty list.")
    return guitars


def display_guitars(guitars):
    """Display all guitars in the list."""
    for i, guitar in enumerate(guitars, 1):
        vintage_string = " (vintage)" if guitar.is_vintage() else ""
        print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")


def add_new_guitars(guitars):
    """Allow user to add new guitars."""
    print("\nEnter your new guitars (leave name blank to finish):")
    while True:
        name = input("Name: ").strip()
        if not name:
            break
        try:
            year = int(input("Year: "))
            cost = float(input("Cost: $"))
            guitar = Guitar(name, year, cost)
            guitars.append(guitar)
            print(f"{guitar} added.\n")
        except ValueError:
            print("Invalid input. Please enter valid year and cost.\n")


def save_guitars(guitars):
    """Save all guitars to guitars.csv file."""
    with open('guitars.csv', 'w') as file:
        for guitar in guitars:
            file.write(f"{guitar.name},{guitar.year},{guitar.cost}\n")


if __name__ == '__main__':
    main()
