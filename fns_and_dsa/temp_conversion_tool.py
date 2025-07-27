#This script will define functions to convert temperatures between Celsius and Fahrenheit, demonstrating the use of global variables to store conversion factors that are accessible within functions.

farherenheit_to_celsius_factor = 5.0 / 9.0
celsius_to_fahrenheit_factor = 9.0 / 5.0

temperature = float(input("Enter temperature: "))
unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

def convert_temperature(temperature, unit):
    global farherenheit_to_celsius_factor, celsius_to_fahrenheit_factor
        
    if unit == 'C':
        # Convert Celsius to Fahrenheit
        converted_temp = (temperature * celsius_to_fahrenheit_factor) + 32
        print(f"{temperature}°C is {converted_temp:.2f}°F")
    elif unit == 'F':
        # Convert Fahrenheit to Celsius
        converted_temp = (temperature - 32) * farherenheit_to_celsius_factor
        print(f"{temperature}°F is {converted_temp:.2f}°C")
    else:
        print("Invalid unit. Please enter C for Celsius or F for Fahrenheit.")
convert_temperature(temperature, unit)
# This code defines a temperature conversion tool that converts between Celsius and Fahrenheit based on user input.
