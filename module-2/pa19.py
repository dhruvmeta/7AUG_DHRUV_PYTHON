def reverse_string_if_multiple_of_4(input_string):
    if len(input_string) % 4 == 0:
        return input_string[::-1]  # Reverse the string if its length is a multiple of 4
    else:
        return input_string  # Return the original string if not a multiple of 4

# Example usage:
input_str = "abcd1234"
result_str = reverse_string_if_multiple_of_4(input_str)
print("Result:",result_str)