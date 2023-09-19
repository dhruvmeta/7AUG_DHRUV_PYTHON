# Input a string from the user
input_string = input("Enter a string: ")

# Check if the string length is at least 3 and ends with 'ing'
if len(input_string) >= 3 and input_string.endswith('ing'):
    # If it ends with 'ing', add 'ly'
    result_string = input_string + 'ly'
elif len(input_string) >= 3:
    # If the length is at least 3, add 'ing'
    result_string = input_string + 'ing'
else:
    # If the length is less than 3, leave it unchanged
    result_string = input_string

print("Result:",result_string)