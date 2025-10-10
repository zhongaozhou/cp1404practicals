"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    subject_records = load_subject_data(FILENAME)
    display_details(subject_records)


def load_subject_data(filename=FILENAME):
    """Read data from file formatted like: subject,lecturer,number of students and return a list."""
    subject_records = []
    input_file = open(filename)
    for line in input_file:
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        subject_records.append(parts)  # Add the record to list of subjects
    input_file.close()
    return subject_records


def display_details(subject_records):
    """Display the subject details including name, lecturer and number of students."""
    for record in subject_records:
        subject, lecturer, num_students = record
        print(f"{subject} is taught by {lecturer} and has {num_students} students")


main()
