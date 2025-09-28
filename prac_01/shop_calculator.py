"""
CP1404/CP5632 - Practical
Shop Calculator
"""

DISCOUNT_RATE = 0.9
DISCOUNT_PRICE = 100

number_of_items = int(input("Number of items: "))
while number_of_items < 0:
    print("Invalid number of items!")
    number_of_items = int(input("Number of items: "))

total_price = 0
for i in range(number_of_items):
    price = float(input("Price of item: "))
    while price < 0:
        print("Invalid price!")
        price = float(input("Price of item: "))
    total_price += price

if total_price > DISCOUNT_PRICE:
    total_price *= DISCOUNT_RATE
print(f"Total price for {number_of_items} items is ${total_price:.2f}")
