print("MPG (USA) to L/100Km (CANADA)")
print("-=" * 30)
userFuel = float(input ("Tell me an amount of fuel (miles per gallon): "))
print("-=" * 30)
calKpLiter = (userFuel * 1.60934) / 3.78541
calKpHundred = calKpLiter * 100

print(f"The value of {userFuel} MPG converted to k/100L is: {calKpHundred:.2f}.")