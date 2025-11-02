"""CP1404/CP5632 Practical - Client code to use the ProgrammingLanguage class.
Estimated time: 15 minutes
Actual time: 20
"""

from prac_06.programming_language import ProgrammingLanguage


def main():
    """Demo test code to show how to use ProgrammingLanguage class."""

    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

    print(python)

    # Create a list of languages
    languages = [python, ruby, visual_basic]

    print("\nThe dynamically typed languages are:")
    for language in languages:
        if language.is_dynamic():
            print(language.name)


main()
