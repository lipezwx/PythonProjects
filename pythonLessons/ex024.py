print("Time Duration in Seconds Machine")
print("-=" * 30)

days = int(input ("Inform a number of days: "))
hours = int(input ("Inform a number of hours: "))
minutes = int(input ("Inform a number of minutes: "))
seconds = int(input ("Inform a number of seconds: "))

convDays = days*24*60*60
convHours = hours*60*60
convMinutes = minutes*60

result = convDays+convHours+convMinutes+seconds

print("-=" * 30)
print(f"The total duration of this period in seconds is: {result}s")