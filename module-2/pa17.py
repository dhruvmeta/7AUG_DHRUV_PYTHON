 #Input a string from the user
input_string = input("Enter a string: ")

# Find the first occurrence of 'not' and 'poor'
not_index = input_string.find('not')
poor_index = input_string.find('poor')

# Check if 'not' and 'poor' are both found and 'not' comes after 'poor'
if not_index != -1 and poor_index != -1 and not_index > poor_index:
    # Replace the 'not'...'poor' substring with 'good'
    result_string = input_string[:poor_index] + 'good' + input_string[not_index + 3:]
else:
    # If not found or 'not' doesn't come after 'poor', keep the original string
    result_string = input_string

print("Result:",result_string)