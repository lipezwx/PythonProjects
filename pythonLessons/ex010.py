import math as mt

print("Arithmetic Calculator")
print("-=" * 30)
numberA = int(input ("Insert an A integer: "))
numberB = int(input ("Insert an B integer: "))
print("-=" * 30)
print(f"The sum of {numberA} and {numberB} is equal to: {numberA+numberB}")
print(f"The difference of {numberA} and {numberB} is equal to: {numberA-numberB}")
print(f"The product of {numberA} and {numberB} is equal to: {numberA*numberB}")
print(f"The quotient of {numberA} and {numberB} is equal to: {numberA/numberB}")
print(f"The remainder when {numberA} is divided by {numberB} is of: {numberA%numberB}")
print(f"The log10 of {numberA} is of: {mt.log10(numberA)}")
print(f"The result of {numberA} elevated by {numberB} is: {numberA**numberB}")