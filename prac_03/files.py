"""
CP1404/CP5632 - Practical
Files
"""

# 1. Write code that asks the user for their name
name = input("Enter your name: ")
out_file = open("name.txt", "w")
print(name, file=out_file)
out_file.close()


# 2. Read the name from name.txt and greet the user
in_file = open("name.txt", "r")
name = in_file.read().strip()
in_file.close()
print(f"Hi {name}!")


# 3. Read first two numbers from numbers.txt and print sum
with open("numbers.txt", "r") as in_file:
    first_number = int(in_file.readline())
    second_number = int(in_file.readline())
    total = first_number + second_number
print(total)


# 4. Print the total for all numbers in numbers.txt
total = 0
with open("numbers.txt", "r") as in_file:
    for line in in_file:
        total += int(line)
print(total)
