print("Heat Capacity Calculus")
print("-=" * 30)
waterMass = float(input ("Please insert the mass of water (grams): "))
tempChange = float(input ("Now, Insert the variability of temperature (ΔT): "))
heatCapacity = waterMass*4.186*tempChange
coffeeCost = (200*4.186*tempChange) / 3600000 * 8.9

print("-=" * 30)
print(f"The total amount of energy required to reach this temperature change is: {heatCapacity:.2f}")
print(f"The cost of boiling water for a cup of coffee (200ml) is: ${coffeeCost:.2f}")