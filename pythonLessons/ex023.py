import math

print("Regular Polygon Area Calculator")
print("-=" * 30)

sideLength = int(input ("Inform the polygon's side lenght: "))
sideNumber = int(input ("Inform the how many sides does the polygon have: "))

areaCalculus = (sideNumber*sideLength**2) / (4 * math.tan(math.pi/sideNumber))

print("-=" * 30)
print(f"The area of this regular polygon is: {areaCalculus:.2f}")