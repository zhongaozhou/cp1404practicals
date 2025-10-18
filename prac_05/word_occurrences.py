"""
CP1404/CP5632 Practical
Word Occurrences
Estimate: 20 minutes
Actual:   30 minutes
"""

# Ask the user for input text
text = input("Text: ")

# Split the text into words
words = text.split()

# Create a dictionary to count word occurrences
word_to_count = {}
for word in words:
    word = word.lower()
    if word in word_to_count:
        word_to_count[word] += 1
    else:
        word_to_count[word] = 1

# Find the length of the longest word
max_length = 0
for word in word_to_count:
    if len(word) > max_length:
        max_length = len(word)


# Sort the dictionary by key and print the results
for word in sorted(word_to_count):
    print(f"{word:{max_length}} : {word_to_count[word]}")
