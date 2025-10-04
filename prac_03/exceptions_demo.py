"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
Answer: When the user enters something that cannot be converted to an integer, such as a sting or a symbol.
2. When will a ZeroDivisionError occur?
Answer: When the user enters 0 for the denominator
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
Answer: Yes. We can use a loop to repeatedly ask for a non-zero denominator.
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        print("Denominator cannot be zero. Please enter a non-zero value:")
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
# except ZeroDivisionError:
#     print("Cannot divide by zero!")
print("Finished.")
