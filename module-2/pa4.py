# Print all even numbers from 1 to 10 using a for loop
for num in range(1, 11):
    if num % 2 == 1:  # Skip odd numbers
        continue
print(num)