def perform_operation (num1, num2, operation):
    # Perform the operation based on user input
    if operation == 'add':
        result = num1 + num2
    elif operation == 'subtract':
        result = num1 - num2
    elif operation == 'multiply':
        result = num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            return "Error: Division by zero is not allowed."
        result = num1 / num2
    else:
        return "Error: Invalid operation. Please choose from add, subtract, multiply, or divide."
    return f"Result: {result}"

if __name__ == "__main__":
    print(perform_operation(0, 0, ''))  # Initial call to trigger user input
# This code defines a function to perform basic arithmetic operations based on user input.