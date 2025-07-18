# Prompt the user to input the size of the pattern
# Note: This version assumes the user will always enter a valid positive integer.
size = int(input("Enter the size of the pattern: "))

# Initialize a counter for the while loop (for rows)
row_count = 0

# Use a while loop to iterate through each row of the pattern
while row_count < size:
    # Use a for loop to print asterisks side by side for the current row
    for _ in range(size):
        print("*", end="")
    
    # After completing each row, print a newline character to move to the next row
    print()
    
    # Increment the row counter
    row_count += 1
