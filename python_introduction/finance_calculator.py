income = input("Enter your monthly income: ")
income = int(income)
expenses = input("Enter your monthly expenses: ")
expenses = int(expenses)
monthly_savings = income - expenses
# Calculate projected savings with 5% annual interest (compounded monthly)
annual_interest_rate = 0.05
monthly_interest_rate = annual_interest_rate / 12

# Calculate monthly savings with interest
monthly_savings_with_interest = monthly_savings * (1 + monthly_interest_rate)

# Calculate total savings after 12 months
projected_savings = monthly_savings_with_interest * 12
print("Your monthly saving are", monthly_savings)
print("Projected savings after one year, with interest is:", projected_savings)
