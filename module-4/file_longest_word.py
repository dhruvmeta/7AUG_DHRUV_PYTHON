# Write a python program to find the longest words. 

with open('globalwarming.txt', 'r') as f:
    str= f.read()
    word_list = str.split()

longest_word = max(word_list)
pos = str.index(longest_word)
print("Longest word: ",longest_word)
print("Position of Longest word: ", pos)