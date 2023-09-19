# Input a letter from the user
letter = input("Enter a letter: ")

# Convert the letter to lowercase to handle both cases
letter = letter.lower()

# Check if the letter is a vowel
if letter in ('a', 'e', 'i', 'o', 'u'):
    print(f"{letter} is a vowel.")
else:
    print(f"{letter} is not a vowel.")