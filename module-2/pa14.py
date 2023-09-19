import collections

# Input a sentence from the user
sentence = input("Enter a sentence: ")

# Split the sentence into words
words = sentence.split()

# Create a Counter object to count word occurrences
word_counter = collections.Counter(words)

# Display word frequencies
for word, frequency in word_counter.items():
    print(f"'{word}' occurs {frequency} time(s) in the sentence.")