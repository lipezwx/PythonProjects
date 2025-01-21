print("Centimeter Height Measure")
print("-=" * 30)
feetMeasure = int(input ("Please tell me your feets measure: "))
inchesMeasure = int(input ("Please tell me your inches measure: "))
feetToInches = feetMeasure * 12
inchesToCentimeters = inchesMeasure * 2.54
print(f"Your total height converted to centimeters is: {feetToInches+inchesToCentimeters}")