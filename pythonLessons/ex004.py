print("Feet to Acres Conversor")
print("-=" * 30)
width = float(input ("Please insert the width of the farmer's field (feet): "))
length = float(input ("Please insert the length of the farmer's field (feet): "))
print("-=" * 30)
final_result = (width * length) * 43560
print(f"The farmer's field total area in acres will be: {final_result:.2f}")