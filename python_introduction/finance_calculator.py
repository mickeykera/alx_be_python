income = input("Enter your monthly income: ")
income = int(income)
expenses = input("Enter your monthly expenses: ")
expenses = int(expenses)
monthly_savings = income - expenses
projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)
print("Your monthly saving are", monthly_savings)
print("Projected savings after one year, with interest is:", projected_savings)
