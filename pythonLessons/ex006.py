print("The Steak Paradise")
print("-=" * 30)
meal_cost = float(input ("What is the cost of the choosen meal? "))
tax = 11.3 / 100
tip = 18 / 100
total_cost = meal_cost + (meal_cost * tax) + (meal_cost * tip)
print("-=" * 30)
print(f"The tax cost of your meal was of: {meal_cost * tax:.2f}")
print(f"The tip cost of your meal was of: {meal_cost * tip:.2f}")
print(f"The total cost of your meal was of: {total_cost:.2f}")
print("-=" * 30)