"""Password check with functions."""

MINIMUM_LENGTH = 8


def main():
    password = get_password()
    print_asterisks(password)


def get_password():
    """Get a valid password."""
    password = input(f"Enter your password (at least {MINIMUM_LENGTH} characters): ")
    while len(password) < MINIMUM_LENGTH:
        print("The password length is less than 8!")
        password = input(f"Enter your password (at least {MINIMUM_LENGTH} characters): ")
    return password


def print_asterisks(password, symbol="*"):
    """Print asterisks equal to the length of the password."""
    print(symbol * len(password))


main()
