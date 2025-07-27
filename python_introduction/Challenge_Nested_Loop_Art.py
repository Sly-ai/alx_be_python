"""Challenge: Nested Loop Art!

Let’s create some text-based art using nested loops! Here’s the idea:

    You’ll write a program that uses nested while loops to print a pyramid pattern of asterisks (*).

Steps:

    Define the height of the pyramid (number of rows) as a variable, for example: rows = 5.
    Use nested while loops to achieve the following:
        The outer loop will control the number of rows.
        The inner loop will print spaces and then asterisks in each row, creating a triangular shape.
    Remember to adjust the number of spaces and asterisks printed within the inner loop based on the current row number to form the pyramid.
"""

rows = 5
i = 1
while i <= rows:
    j = 1
    # Print spaces before the asterisks
    while j <= rows - i:
        print(" ", end="")
        j += 1
    
    k = 1
    # Print asterisks for the current row
    while k <= (2 * i - 1):
        print("*", end="")
        k += 1
    
    print()  # Move to the next line after each row
    i += 1  # Move to the next row
    