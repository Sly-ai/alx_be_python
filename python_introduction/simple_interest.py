principal = 1000  # Principal amount in dollars
rate = 0.05  # Interest rate in percent
time = 3  # Time in years
def calculate_simple_interest(principal, rate, time):
    return (principal * rate * time)
def main():
    interest = calculate_simple_interest(principal, rate, time)
    print("The Simple Interest is:", interest)
if __name__ == "__main__":
    main()
# This code calculates simple interest based on principal, rate, and time.