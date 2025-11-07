"""
CP1404/CP5632 Practical
ProgrammingLanguage class
Estimate: 30 minutes
Actual: 30 minutes
"""


class ProgrammingLanguage:
    """Represent a ProgrammingLanguage object."""

    def __init__(self, name, typing, reflection, year):
        """Initialise a ProgrammingLanguage instance.

        name: string, name of the language
        typing: string, either 'Static' or 'Dynamic'
        reflection: boolean, whether the language supports reflection
        year: integer, year the language first appeared
        """
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """Return True if the language is dynamically typed, False if not."""
        return self.typing.lower() == "dynamic"

    def __str__(self):
        """Return a string of the ProgrammingLanguage instance."""
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"
