"""
CP1404/CP5632 Practical - Project Management program.
Estimated time: 90 minutes
Actual time: 120 minutes
"""

import datetime
from project import Project

FILENAME = "projects.txt"


def main():
    """Main program for project management."""
    # projects = []
    print("Welcome to Pythonic Project Management")

    # Load projects from default file
    projects = load_projects(FILENAME)
    # print(f"Loaded {len(projects)} projects from {FILENAME}")

    menu_choice = ""
    while menu_choice != "q":
        display_menu()
        menu_choice = input(">>> ").lower()

        if menu_choice == "l":
            filename = input("Enter filename to load from: ")
            projects = load_projects(filename)
        elif menu_choice == "s":
            filename = input("Enter filename to save to: ")
            save_projects(filename, projects)
        elif menu_choice == "d":
            display_projects(projects)
        elif menu_choice == "f":
            filter_projects_by_date(projects)
        elif menu_choice == "a":
            add_new_project(projects)
        elif menu_choice == "u":
            update_project(projects)
        elif menu_choice == "q":
            if confirm_save():
                save_projects(FILENAME, projects)
            print("Thank you for using custom-built project management software.")
        else:
            print("Invalid menu choice")


def display_menu():
    """Display the main menu."""
    print("- (L)oad projects")
    print("- (S)ave projects")
    print("- (D)isplay projects")
    print("- (F)ilter projects by date")
    print("- (A)dd new project")
    print("- (U)pdate project")
    print("- (Q)uit")


def load_projects(filename):
    """Load projects from file."""
    projects = []
    try:
        with open(filename, 'r') as file:
            # Skip header line
            file.readline()
            for line in file:
                parts = line.strip().split('\t')
                if len(parts) == 5:
                    name = parts[0]
                    start_date = parts[1]
                    priority = int(parts[2])
                    cost_estimate = float(parts[3])
                    completion_percentage = int(parts[4])
                    project = Project(name, start_date, priority, cost_estimate, completion_percentage)
                    projects.append(project)
        print(f"Loaded {len(projects)} projects from {filename}")
    except FileNotFoundError:
        print(f"File {filename} not found. Starting with empty project list.")
    return projects


def save_projects(filename, projects):
    """Save projects to file."""
    with open(filename, 'w') as file:
        file.write("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage\n")
        for project in projects:
            file.write(f"{project.name}\t{project.start_date}\t{project.priority}\t"
                       f"{project.cost_estimate}\t{project.completion_percentage}\n")
    print(f"Saved {len(projects)} projects to {filename}")


def display_projects(projects):
    """Display projects grouped by completion status."""
    incomplete_projects = [p for p in projects if not p.is_complete()]
    complete_projects = [p for p in projects if p.is_complete()]

    incomplete_projects.sort()
    complete_projects.sort()

    print("Incomplete projects: ")
    for project in incomplete_projects:
        print(f"  {project}")

    print("Completed projects: ")
    for project in complete_projects:
        print(f"  {project}")


def filter_projects_by_date(projects):
    """Filter and display projects starting after a given date."""
    date_string = input("Show projects that start after date (dd/mm/yyyy): ")
    try:
        filter_date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
        filtered_projects = []

        for project in projects:
            project_date = datetime.datetime.strptime(project.start_date, "%d/%m/%Y").date()
            if project_date >= filter_date:
                filtered_projects.append(project)

        # Sort by date
        filtered_projects.sort(key=lambda p: datetime.datetime.strptime(p.start_date, "%d/%m/%Y"))

        for project in filtered_projects:
            print(project)

    except ValueError:
        print("Invalid date format. Please use dd/mm/yyyy.")


def add_new_project(projects):
    """Add a new project."""
    print("Let's add a new project")
    name = input("Name: ")
    start_date = input("Start date (dd/mm/yyyy): ")
    priority = int(input("Priority: "))
    cost_estimate = float(input("Cost estimate: $"))
    completion_percentage = int(input("Percent complete: "))

    project = Project(name, start_date, priority, cost_estimate, completion_percentage)
    projects.append(project)
    print(f"Added {name} to projects.")


def update_project(projects):
    """Update an existing project."""
    print("Choose a project to update:")
    for i, project in enumerate(projects):
        print(f"{i} {project}")

    try:
        choice = int(input("Project choice: "))
        if 0 <= choice < len(projects):
            project = projects[choice]
            print(project)

            new_percentage = input("New Percentage: ")
            if new_percentage:
                project.completion_percentage = int(new_percentage)

            new_priority = input("New Priority: ")
            if new_priority:
                project.priority = int(new_priority)

            print("Project updated.")
        else:
            print("Invalid project choice.")
    except ValueError:
        print("Please enter a valid number.")


def confirm_save():
    """Ask user if they want to save before quitting."""
    response = input(f"Would you like to save to {FILENAME}? ").lower()
    return response.startswith('y')


if __name__ == '__main__':
    main()
