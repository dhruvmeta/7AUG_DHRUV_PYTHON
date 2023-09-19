# Input two numbers from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Swap the numbers without a temporary variable
num1 = num1 + num2
num2 = num1 - num2
num1 = num1 - num2

print("After swapping (without temp variable):")
print("First number:", num1)
print("Second number:",num2)