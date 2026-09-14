#Aiden Frye
#September 14, 2026
#P1HW2
#Purpose: This program will help the user budget for travel expenses

#Ask the user for their budget, destination, and expenses
budget = float(input("Please enter your budget for the trip: $"))
print()

destination = input("Please input where you wish to travel to: ")
print()

gas_expense = float(input("Please enter your estimated gas costs for this trip: $"))
print()

food_expense = float(input("Please enter your estimated cost to eat: $"))
print()

housing_expense = float(input("Lastly, please enter your estimated cost for housing: $"))
print()

#Calculate and display the location of travel, total expenses, and remaining budget
print()
print(budget)
print(f"You wish to travel to {destination}.")
print()

print(f"Your estimated gas costs are: ${gas_expense:.2f}")
print(f"Your estimated food costs are: ${food_expense:.2f}")
print(f"Your estimated housing costs are: ${housing_expense:.2f}")
print()

total_expenses = gas_expense + food_expense + housing_expense
print(f"Total estimated expenses for this trip are: ${total_expenses:.2f}")
print()

remaining_budget = budget - (gas_expense + food_expense + housing_expense)
print(f"Your remaining budget after expenses is: ${remaining_budget:.2f}")