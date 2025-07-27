#This script will define functions to convert temperatures between Celsius and Fahrenheit, demonstrating the use of global variables to store conversion factors that are accessible within functions.

FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR  = 9/5

# This code defines a temperature conversion tool that converts between Celsius and Fahrenheit based on user input.
temperature = float(input("Enter the temperature to convert: "))
if temperature != float(temperature):
    raise ValueError("Invalid temperature. Please enter a numeric value.")
unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

def convert_temperature(temperature, unit):
    global FAHRENHEIT_TO_CELSIUS_FACTOR, CELSIUS_TO_FAHRENHEIT_FACTOR 
        
    if unit == 'C':
        # Convert Celsius to Fahrenheit
        converted_temp = (temperature * CELSIUS_TO_FAHRENHEIT_FACTOR ) + 32
        print(f"{temperature}°C is {converted_temp:.2f}°F")
    elif unit == 'F':
        # Convert Fahrenheit to Celsius
        converted_temp = (temperature - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
        print(f"{temperature}°F is {converted_temp:.2f}°C")
    else:
        print("Invalid unit. Please enter C for Celsius or F for Fahrenheit.")
convert_temperature(temperature, unit)
# This code defines a temperature conversion tool that converts between Celsius and Fahrenheit based on user input.
