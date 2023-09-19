# Input a string from the user
input_string = input("Enter a string: ")

# Input the substring to count
substring = input("Enter the substring to count: ")

# Use the count() method to count occurrences of the substring
count = input_string.count(substring)

print(f"The substring '{substring}' occurs {count} times in the string.")