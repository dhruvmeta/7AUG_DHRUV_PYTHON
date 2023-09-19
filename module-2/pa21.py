def insert_string_in_middle(base_string, insert_string):
    # Calculate the midpoint index of the base string
    mid_index = len(base_string) // 2
    
    # Insert the insert_string in the middle of the base_string
    result_string = base_string[:mid_index] + insert_string + base_string[mid_index:]
    
    return result_string

# Example usage:
base_str = "Hello, World!"
insert_str = "Python"
result_str = insert_string_in_middle(base_str, insert_str)
print("Result:",result_str)