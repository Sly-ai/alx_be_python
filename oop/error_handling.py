class ZeroDivisionError(Exception):
    """Custom exception for division by zero errors."""
    def __init__(self, message="Division by zero is not allowed."):
        self.message = message
        super().__init__(self.message)
class ValueError(Exception):
    """Custom exception for value errors."""
    def __init__(self, message="Invalid value provided."):
        self.message = message
        super().__init__(self.message)
class Exception(Exception):
    """Base class for all exceptions."""
    def __init__(self, message="An error occurred."):
        self.message = message
        super().__init__(self.message)

def divide_numbers(numerator, denominator):
    """Function to divide two numbers with error handling."""
    if denominator == 0:
        raise ZeroDivisionError()
    elif not isinstance(numerator, (int, float)) or not isinstance(denominator, (int, float)):
        raise ValueError("Both numerator and denominator must be numbers.")
    elif numerator < 0 or denominator < 0:
        raise ValueError("Both numerator and denominator must be non-negative.")
    else:   
        return numerator / denominator

def main():
    try:
        num = input("Enter numerator: ")
        denom = input("Enter denominator: ")
        result = divide_numbers(num, denom)
        print(f"Result: {result}")
    except ZeroDivisionError as e:
        print(e.message)
    except ValueError as e:
        print(e.message)
    except Exception as e:
        print(e.message)
if __name__ == "__main__":
    main()