print("Ideal Gas Law Calculator")
print("-=" * 30)

pressureGas = int(input ("Inform the pressure of the evaluated gas (Pascal): "))
volumeGas = int(input ("Inform the volume of the evaluated gas (Liters): "))
tempGas = float(input ("Inform the temperature of the evaluated gas (Celsius): "))

celsiusToKelvin = tempGas + 273.15
molesCalculus = (pressureGas*volumeGas) / (8.314 * celsiusToKelvin)

print("-=" * 30)
print(f"The content of moles in this gas is: {molesCalculus:.2f}")