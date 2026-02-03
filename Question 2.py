score=int(input("What's your creditscore? "))

if score< 300 or score> 850:
    print("Invalid credit score.")
elif score >= 750:
    print("Excellent credit - Loan Approved. Interest rate: Low")
elif score >= 700:
    print("Good credit - Loan Approved with Review. Interest rate: Low to Moderate")
elif score >= 600:
    print("Fair credit - Loan Conditional. Seek credit improvement.")
else:
    print("Poor credit - Loan Denied. Seek credit improvement.")