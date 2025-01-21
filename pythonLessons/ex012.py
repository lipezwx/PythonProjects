import math
import numpy

print("Distance between points in earth surface.")
print("-=" * 30)

latitudeA = float(input ("Please insert the latitude of point A: "))
longitudeA = float(input ("Please insert the longitude of point A: "))
print("-=" * 30)
latitudeB = float(input ("Please insert the latitude of point B: "))
longitudeB = float(input ("Please insert the longitude of point B: "))

latitudeA = math.radians(latitudeA)
latitudeB = math.radians(latitudeB)
longitudeA = math.radians(longitudeA)
longitudeB = math.radians(longitudeB)


distance = 6371.01 * numpy.arccos(math.sin(latitudeA) * math.sin(latitudeB) + math.cos(latitudeA) * math.cos(latitudeB) * math.cos(longitudeA - longitudeB))

print(f"The distance between point A and B is: {distance:.2f} degrees.")