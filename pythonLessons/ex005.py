small_container = int(input ("How many drink containers of 1 liter do you have? "))
big_container = int(input ("How many drink containers of more than 1 liter do you have? "))

small_refund = small_container * 0.10
big_refund = big_container * 0.25

final_result = small_refund + big_refund

print("-=" * 30)
print(f"If you recycle these containers the refund would be of: ${final_result}")