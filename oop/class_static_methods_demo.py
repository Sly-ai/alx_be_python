# class_static_methods_demo.py

class Calculator:
    # Class attribute
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """
        Static method to return the sum of two numbers.
        Does not access class or instance data.
        """
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """
        Class method to return the product of two numbers.
        Uses 'cls' to access class attributes.
        """
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
