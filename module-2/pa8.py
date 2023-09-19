# Input three integers from the user
num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))
num3 = int(input("Enter the third integer: "))

# Check if any two values are equal
if num1 == num2 or num2 == num3 or num1 == num3:
    sum_result = 0
else:
    sum_result = num1 + num2 + num3

print("The sum is:",sum_result)