number1 = 10
number2 = 5
def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b

def main():
    print("Addition:", add(number1, number2))
    print("Subtraction:", subtract(number1, number2))
    print("Multiplication:", multiply(number1, number2))
    print("Division:", divide(number1, number2))
if __name__ == "__main__":
    main()
# This code performs basic arithmetic operations: addition, subtraction, multiplication, and division.
# It defines functions for each operation and uses them in a main function to demonstrate their usage.