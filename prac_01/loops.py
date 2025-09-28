"""
CP1404/CP5632 - Practical
Loops
"""

for i in range(1, 21, 2):
    print(i, end=' ')
print()

# a
for i in range(0, 110, 10):
    print(i, end=' ')
print()

# b
for i in range(20, 0, -1):
    print(i, end=' ')
print()

# c
number_of_stars = int(input("Number of stars: "))
for i in range(number_of_stars + 1):
    print("*", end='')
print()

# d
num_of_lines = int(input("Number of lines: "))
for rows in range(1, num_of_lines + 1):
    for columns in range(rows):
        print("*", end='')
    print()
