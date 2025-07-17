pattern = int(input("Enter the size of the pattern: "))

for i in range(pattern):
    for j in range(pattern):
        print("*", end="")
    print()  # Move to the next line after each row
print()  # Print an extra line after the pattern
print("Pattern drawing complete.")

