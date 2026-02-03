def get_tax_bracket(income):
    if income < 0:
        return "Invalid income", 0

    if income < 50000:
        bracket = "Low (10%)"
        rate = 0.10
    elif income < 100000:
        bracket = "Medium (20%)"
        rate = 0.20
    else:
        bracket = "High (30%)" 
        rate = 0.30

    bracket = bracket + " (Deduction Eligible)" if income % 2 == 0 else bracket
    return bracket, rate

#Main Program
annual_income = float(input("What is your annual income: "))
bracket, rate = get_tax_bracket(annual_income)
if bracket == "Invalid income":
    print("Invalid Bracket.")
else:
    estimated_tax = annual_income * rate
    print(f"Your tax bracket is: {bracket}. Estimated tax: ${estimated_tax:.2f}")
   