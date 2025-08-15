#Q12. Ask the user for their income and calculate tax.

income = int(input("Enter your income: "))

tax = None

if income <= 0:
    print(f"You Enter Insufficient Amount {income}")
else:
    if income > 0 and income < 250000:
        tax = 0
    elif income >= 250000 and income < 500000:
        tax = income * 0.05
    elif income >= 500000 and income <= 1000000:
        tax = income * 0.20
    elif income > 1000000:
        tax = income * 0.30

    print(f"Your Income: {income}")
    print(f"Calculated Tax: {tax}")
    print(f"Net Income after Tax: {income - tax}")
