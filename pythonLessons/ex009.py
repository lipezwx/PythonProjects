account_balance = float(input ("How much you want to deposit on your savings account? "))

percentage = 4 / 100

print(f"In a period of 1 year you would have the total balance of: ${account_balance+(account_balance * percentage)}")
print(f"In a period of 2 year you would have the total balance of: ${account_balance+(account_balance * (percentage*2))}")
print(f"In a period of 3 year you would have the total balance of: ${account_balance+(account_balance * (percentage*3))}")