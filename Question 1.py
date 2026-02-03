revenue= float(input("What's the revenue? "))
cost= float(input("What's the cost? "))

profit= revenue - cost
if revenue > 0:
    profit_margin= round((profit / revenue) * 100, 2)
    print(f"Profit: ${profit:,.2f} | Margin: {profit_margin:.2f}%")
else:
    print("Invalid revenue value.")