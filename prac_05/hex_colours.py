"""
CP1404/CP5632 Practical
Hexadecimal colour code
"""

# define a constant dictionary of colour names and colour codes
COLOUR_TO_HEX = {
    "absolute zero": "#0048ba",
    "acid green": "#b0bf1a",
    "aliceblue": "#f0f8ff",
    "alizarin crimson": "#e32636",
    "amaranth": "#e52b50",
    "amber": "#ffbf00",
    "amethyst": "#9966cc",
    "antiquewhite": "#faebd7",
    "apricot": "#fbceb1",
    "aqua": "#00ffff"
}

print("Available colours and codes:")
for colour in COLOUR_TO_HEX:
    print(f"{colour.title():<20} : {COLOUR_TO_HEX[colour]}")
print()

colour_name = input("Enter colour name: ").lower()
while colour_name != "":
    try:
        print(f"The code for {colour_name.title()} is {COLOUR_TO_HEX[colour_name]}")
    except KeyError:
        print("Invalid colour name.")
    colour_name = input("Enter a colour name: ").lower()
