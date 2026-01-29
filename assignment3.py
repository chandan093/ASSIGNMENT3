# Function to calculate factorial using recursion
def factorial(n):
    if n == 0 or n == 1:   # Base case
        return 1
    else:
        return n * factorial(n - 1)   # Recursive case

# Call the function with a sample number
sample_number = 5
result = factorial(sample_number)

# Print the output
print(f"The factorial of {sample_number} is: {result}")

import math

# Step 1: Ask the user for a number
num = float(input("Enter a number: "))

# Step 2: Perform calculations using math module
square_root = math.sqrt(num)
natural_log = math.log(num)   # log base e
sine_value = math.sin(num)    # input is in radians

# Step 3: Display results
print(f"Square root of {num} is: {square_root}")
print(f"Natural logarithm of {num} is: {natural_log}")
print(f"Sine of {num} radians is: {sine_value}")