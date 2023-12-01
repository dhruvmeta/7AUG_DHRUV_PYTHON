def count_strings_with_same_start_and_end(strings):
    count = 0

    for string in strings:
        if len(string) >= 2 and string[0] == string[-1]:
            count += 1

    return count

# Example usage:
string_list = ["aba", "hello", "world", "level", "racecar"]
result = count_strings_with_same_start_and_end(string_list)

print(f"Number of strings with the same start and end character: {result}")