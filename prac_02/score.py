"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

import random


def main():
    score = float(input("Enter score: "))
    result = determine_score_status(score)
    print(result)

    # Random score check
    random_score = random.randint(0, 100)
    print(f"Random score: {random_score}")
    print(determine_score_status(random_score))


def determine_score_status(score):
    """Determine the result of a score."""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score < 50:
        return "Bad"
    elif score < 90:
        return "Passable"
    else:
        return "Excellent"


main()
