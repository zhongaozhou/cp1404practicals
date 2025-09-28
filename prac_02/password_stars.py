

MINIMUM_LENGTH = 8
password = input("Enter your password(more than 8 numbers or alphabets):")
length = len(password)
while length < MINIMUM_LENGTH:
        print("Unqualified password")
        password = input("Enter your password(more than 8 numbers or alphabets):")
        length = len(password)
print("*" * length)
