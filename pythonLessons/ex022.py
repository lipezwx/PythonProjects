import math

print("Triangle's Area Calculator (By three sides lenght)")
print("-=" * 30)

sideA = int(input ("Please inform the side A lenght of the triangle: "))
sideB = int(input ("Please inform the side B lenght of the triangle: "))
sideC = int(input ("Please inform the side C lenght of the triangle: "))
allSides = (sideA+sideB+sideC)/2

triangleArea = math.sqrt(allSides*(allSides-sideA)*(allSides-sideB)*(allSides-sideC))

print("-=" * 30)
print(f"The total area of the triangle is: {triangleArea}")