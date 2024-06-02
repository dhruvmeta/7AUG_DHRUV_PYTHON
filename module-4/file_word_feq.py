# Write a Python program to count the frequency of words in a file.

with open('globalwarming.txt', 'r') as f:
    line= f.read()

word = input("Enter the word to check it's freq: ")
result = line.count(word)
print("Number of substring occurrences:", result)