import math

print("Free Fall Spd Calculator")
print("-=" * 30)

heightObject = int(input ("Insert the height which the object will be dropped (meters): "))
vfCalculus = math.sqrt(0**2+2*9.8*heightObject)

print("-=" * 30)
print(f"The speed which the object will fall would be: {vfCalculus:.2f}")