total = 0
expenses = []
for i in range(7):
    expenses.append(float(input("Enter an expense\n")))

total = sum(expenses)

print("You spent $", total, " on lunch this week.", sep='')