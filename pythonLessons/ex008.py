print("Gizmos and Widgets Store")
print("-=" * 30)
widgets = int(input ("How many widgets have you bought (grams) ? "))
gizmos = int(input ("How many gizmos have you bought (grams) ? "))

weight_widgets = widgets*75
weight_gizmos = gizmos*112

print("-=" * 30)
print(f"The total weight of your order is of: {weight_widgets+weight_gizmos} grams.")