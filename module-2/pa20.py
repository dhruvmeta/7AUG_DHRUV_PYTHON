def get_first_and_last_2_chars(input_string):
    if len(input_string) < 2:
        return ""  # Return an empty string if the length is less than 2
    else:
        return input_string[:2] + input_string[-2:]

# Example usage:
input_str = input("Enter a string: ")
result_str = get_first_and_last_2_chars(input_str)
print("Result:",result_str)