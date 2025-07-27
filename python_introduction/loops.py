"""Challenge

Numbers can add up quickly! Write a Python program using a for loop to calculate the sum of all the numbers in a list.

    Create a list of numbers (e.g., numbers = [1, 5, 3, 9]).
    Initialize a variable total to 0, which will store the running sum.
    Use a for loop to iterate over the numbers list.
    Inside the loop, add the current number (use the loop variable) to the total variable.
    After the loop, print the final total value, which represents the sum of all the numbers in the list."""

rows = 5

for i in range(1, rows + 1):
  # Outer loop controls the number of rows
  for j in range(1, i + 1):
    # Inner loop prints asterisks for each row
    print("*", end="")
  print()  # Move to a new line after each row of asterisks


