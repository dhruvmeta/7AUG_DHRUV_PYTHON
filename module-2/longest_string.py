

import string


string1 = input ("please enter a words :")

long_str = 0

for word in string.split():
    if len(word) > long_str:
        long_str = len(word)
        long_word =word
print(f" the longest word is {long_word}with length ", len (long_word))
