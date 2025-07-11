import datetime

year = datetime.date.today().year
future_years = int(input("How many years into the future do you want to calculate your age: "))
age = input("How old are you: ")

future_age = int(age) + future_years
print(f"Current Year: {year}")
print(f"In {future_years+year}, you will be {future_age} years old.")
# This code calculates a person's age in a specified number of years into the future. It uses the current year and the user's current age to compute the future age.
