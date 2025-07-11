interest = 0.05

monthly_income = float(input("Enter your monthly income: "))
monthly_expenses = float(input("Enter your monthly expenses: "))
def calculate_savings(income, expenses):
    monthly_savings = income - expenses
    projected_savings = monthly_savings * 12 + (monthly_savings * interest * 12)
    return monthly_savings, projected_savings
def main():
    monthly_savings, projected_savings = calculate_savings(monthly_income, monthly_expenses)
    print(f"Your monthly savings are: ${monthly_savings:.2f}")
    print(f"Projected savings after one year: ${projected_savings:.2f}")
if __name__ == "__main__":
    main()
# This code calculates monthly savings and projects annual savings based on monthly income and expenses, including interest.

