print("Self Checkout Machine")
print("-=" * 30)
userCents = int(input ("How many cents do you want to deposit? "))
while True:
    print("-=" * 30)
    print("0 - Finish Program\n1 - Pennies\n2 - Nickels\n3 - Dimes\n4 - Quarters\n5 - Loonies\n6- Toonies")
    print("-=" * 30)
    userChoice = int(input ("Your option: "))
    if userChoice == 0:
        print("Program finished.")
        break
    if userChoice == 1:
        pennies = userCents * 0.01
        print(f"The equivalent of this amount in a change would be: {pennies} dollars")
    if userChoice == 2:
        nickels = userCents * 0.05
        print(f"The equivalent of this amount in a change would be: {nickels} dollars")
    if userChoice == 3:
        dimes = userCents * 0.10
        print(f"The equivalent of this amount in a change would be: {dimes} dollars")
    if userChoice == 4:
        quarters = userCents * 0.25
        print(f"The equivalent of this amount in a change would be: {quarters} dollars")
    if userChoice == 5:
        loonies = userCents * 1.00
        print(f"The equivalent of this amount in a change would be: {loonies} dollars")
    if userChoice == 6:
        toonies = userCents * 2.00
        print(f"The equivalent of this amount in a change would be: {toonies} dollars")
    if 0 < userChoice > 6:
        print("Choose an valid option !")
