import math

print("Cylinder Volume Calculator")
print("-=" * 30)

cylinderRadius = int(input ("Inform the radius of the evaluated cylinder: "))
cylinderHeight = int(input ("Now, Inform the height of the evaluated cylinder: "))

areaBase = math.pi*cylinderRadius**2
cylinderVolume = areaBase*cylinderHeight

print("-=" * 30)
print(f"The volume of the cylinder is: {cylinderVolume:.1f}")