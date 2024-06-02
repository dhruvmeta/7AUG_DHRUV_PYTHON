# Write a Python program to append text to a file and display the text. 

with open('globalwarming.txt', 'a') as f:
    print(f.write("\nThis is python\n"))