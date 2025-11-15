"""
CP1404/CP5632 Practical - Project class.
Estimated time: 90 minutes
Actual time:
"""


class Project:
    """Represent a Project object."""

    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        """Initialise a Project instance.

        name: string, name of the project
        start_date: string, start date of the project (dd/mm/yyyy)
        priority: integer, priority of the project (lower is higher priority)
        cost_estimate: float, estimated cost of the project
        completion_percentage: integer, percentage completion (0-100)
        """
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def __str__(self):
        """Return a string representation of the Project."""
        return (f"{self.name}, start: {self.start_date}, priority {self.priority}, "
                f"estimate: ${self.cost_estimate:.2f}, completion: {self.completion_percentage}%")

    def __lt__(self, other):
        """Less than comparison for sorting by priority."""
        return self.priority < other.priority

    def is_complete(self):
        """Return True if project is 100% complete, False otherwise."""
        return self.completion_percentage == 100
