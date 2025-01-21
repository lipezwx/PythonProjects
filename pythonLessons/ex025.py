print("Seconds to DD/HH/MM/SS Conversor")
print("-=" * 30)

userSeconds = int(input ("Inform a number of seconds (s): "))

convMinutes = userSeconds/60
convHours = convMinutes/60
convDays = convHours/24

print("-=" * 30)
print(f"Here's the conversion: {convDays:.2f} Days/ {convHours:.2f} Hours/ {convMinutes:.2f} Minutes/ {userSeconds:.2f} Seconds")