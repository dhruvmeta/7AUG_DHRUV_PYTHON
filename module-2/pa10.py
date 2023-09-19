# Input a positive integer 'n' from the user
n = int(input("Enter a positive integer 'n': "))

# Check if 'n' is a positive integer
if n <= 0:
    print("Please enter a positive integer.")
else:
    # Calculate the sum of the first 'n' positive integers using the formula
    sum_of_integers = (n * (n + 1)) // 2

    print(f"The sum of the first {n} positive integers is: {sum_of_integers}")