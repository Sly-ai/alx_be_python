class Calculator:
    Calculation_types = "Arithmetic Operations"
        

    @staticmethod
    def add(a, b):
        """Return the sum of two numbers."""
        return a + b

    @classmethod
    def multiply(cls, a, b):
        print(f"calculation_type:{cls.Calculation_types}")
        """Return the product of two numbers and print the calculation type."""
        return a * b


# Demonstration
if __name__ == "__main__":
    # Using the static method
    sum_result = Calculator.add(10, 5)
    print(f"The sum is: {sum_result}")
    print(f"Calculation type: {Calculator.operations['+']}")

    # Using the class method
    product_result = Calculator.multiply(10, 5)
    print(f"The product is: {product_result}")
    print(f"Calculation type: {Calculator.operations['*']}")
