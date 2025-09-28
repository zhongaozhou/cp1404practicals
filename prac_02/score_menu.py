"""CP1404/CP5632 - Practical
Score menu program with functions.
"""


def main():
    score = get_valid_score()
    display_menu()
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            print(determine_score_result(score))
        elif choice == "S":
            print("*" * int(score))
        else:
            print("Invalid option")
        display_menu()
        choice = input(">>> ").upper()
    print("Farewell!")


def display_menu():
    """Display the menu."""
    print("(G)et a valid score (must be 0-100 inclusive)")
    print("(P)rint result")
    print("(S)how stars")
    print("(Q)uit")


def get_valid_score():
    """Get a valid score between 0 and 100 inclusive."""
    score = float(input("Enter score (0-100): "))
    while score < 0 or score > 100:
        print("Invalid score")
        score = float(input("Enter score (0-100): "))
    return score


def determine_score_result(score):
    """Determine the result of a score."""
    if score < 50:
        return "Bad"
    elif score < 90:
        return "Passable"
    else:
        return "Excellent"


main()
