import math

userRadius = float(input ("Inform the radius of the circumference: "))
circleArea = math.pi*userRadius**2
sphereVolume = 4/3*math.pi*userRadius**3

print("-=" * 30)
print(f"The circle with radius {userRadius} have an area of: {circleArea:.2f}")
print(f"The volume of the sphere with radius {userRadius} is: {sphereVolume:.2f} ")