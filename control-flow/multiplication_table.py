# Prompt the user to input a number
# Note: This version assumes the user will always enter a valid integer.
# Error handling for non-integer input has been removed as per request.
number = int(input("Enter a number to see its multiplication table: "))

# Generate and print the multiplication table using a for loop
print(f"Multiplication table for {number}:")
for i in range(1, 11):  # Iterate from 1 to 10 (inclusive)
    product = number * i
    print(f"{number} * {i} = {product}")
