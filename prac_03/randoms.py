"""CP1404/CP5632 - Practical
Random Numbers
"""
import random

print(random.randint(5, 20))  # line 1
print(random.randrange(3, 10, 2))  # line 2
print(random.uniform(2.5, 5.5))  # line 3


# What did you see on line 1? What was the smallest number you could have seen, what was the largest?
# Answer: A random integer between 5 and 20 inclusive.
# The smallest number is 5, the largest is 20.

# What did you see on line 2? What was the smallest number you could have seen, what was the largest?
# Could line 2 have produced a 4?
# Answer: A random integer chosen from the sequence 3, 5, 7, 9
# The smallest number is 3, the largest number is 9.
# Line 2 could not produce a 4, because step=2 makes only odd numbers (3, 5, 7, 9).

# What did you see on line 3? What was the smallest number you could have seen, what was the largest?
# Answer: A random float between 2.5 and 5.5.
# The smallest is 2.5, the largest is 5.5.

# Write code, not a comment, to produce a random number between 1 and 100 inclusive.
print(random.randint(1, 100))
