# Write a Python function that checks whether a passed string is palindrome or not 

# A palindrome is a word, phrase, or sequence that reads the same backward as forward, 
# e.g., madam or nurses run.

def isPalindrome(s):
    return s == s[::-1]
 
str1 = input("enter a word: ")
ans = isPalindrome(str1)
 
if ans:
    print("Yes")
else:
    print("No")