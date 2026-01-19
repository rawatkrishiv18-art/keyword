bill_amount = float(input("Enter total bill amount: "))
paid_amount = float(input("Enter amount paid by customer: "))

due_amount = bill_amount - paid_amount

if due_amount > 0:
    print("Customer due amount is:", due_amount)

elif due_amount == 0:
    print("No due amount. Bill is fully paid.")

else:
    print("Extra amount paid:", abs(due_amount))
