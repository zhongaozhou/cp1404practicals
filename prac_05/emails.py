"""
CP1404/CP5632 Practical
Emails
Estimate: 25 minutes
Actual:   30 minutes
"""


def main():
    """stores users' emails (unique keys) and names (values) in a dictionary."""
    email_to_name = {}
    email = input("Email: ").strip()

    while email != "":
        name = extract_name(email)
        confirm = input(f"Is your name {name}? (Y/n) ").strip().lower()
        if confirm not in ("", "y"):
            name = input("Name: ").title().strip()

        email_to_name[email] = name
        email = input("Email: ").strip()

    print()
    # Print all names and emails
    for email, name in email_to_name.items():
        print(f"{name} ({email})")


def extract_name(email):
    """
    Extract a person's name from their email.
    """
    prefix = email.split("@")[0]
    parts = prefix.split(".")
    name = " ".join(parts).title()
    return name


main()
