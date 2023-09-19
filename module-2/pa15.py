# Input two strings from the user
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

# Check if both strings have at least 2 characters
if len(string1) < 2 or len(string2) < 2:
    print("Both strings should have at least 2 characters.")
else:
    # Swap the first two characters of each string
    swapped_string1 = string2[:2] + string1[2:]
    swapped_string2 = string1[:2] + string2[2:]

    # Combine the swapped strings with a space in between
    result_string = swapped_string1 + " " + swapped_string2

    print("Result:",result_string)