interest = 0.05

monthly_income = float(input("Enter your monthly income: "))
monthly_expenses = float(input("Enter your monthly expenses: "))

monthly_savings = monthly_income - monthly_expenses
projected_savings = monthly_savings * 12 * (1 + interest)

print(f"Your monthly savings are: ${monthly_savings}")
print(f"Projected savings after one year: ${projected_savings}")

# This code calculates monthly savings and projects annual savings based on monthly income and expenses, including interest.

