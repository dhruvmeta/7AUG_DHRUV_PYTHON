# Function to generate Fibonacci series up to a given range
def generate_fibonacci_series(n):
    fibonacci_series = []
    a, b = 0, 1
    while a <= n:
        fibonacci_series.append(a)
        a, b = b, a + b
    return fibonacci_series

# Input the range from the user
range_limit = int(input("Enter the range for Fibonacci series: "))

if range_limit <= 0:
    print("Please enter a positive range.")
else:
    fibonacci_series = generate_fibonacci_series(range_limit)
    print("Fibonacci series up to", range_limit, ":", fibonacci_series)