print("Distance Units Conversor")
print("-=" * 30)

userMeasure = float(input ("Insert a measurement (feet): "))

print("-=" * 30)
print(f"The measurement {userMeasure} feet in inches is: {userMeasure*12}")
print(f"The measurement {userMeasure} feet in yards is: {userMeasure/3}")
print(f"The measurement {userMeasure} feet in miles is: {(userMeasure/3) / 1760}")