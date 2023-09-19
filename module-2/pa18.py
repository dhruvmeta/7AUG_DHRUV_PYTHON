def find_longest_word_length(word_list):
    if not word_list:
        return 0  # Return 0 if the list is empty

    # Initialize the length of the longest word to the length of the first word
    longest_length = len(word_list[0])

    # Iterate through the remaining words in the list
    for word in word_list[1:]:
        # Update the longest_length if a longer word is found
        if len(word) > longest_length:
            longest_length = len(word)

    return longest_length

# Example usage:
word_list = ["apple", "banana", "cherry", "date"]
longest_length = find_longest_word_length(word_list)
print("The length of the longest word is:",longest_length)