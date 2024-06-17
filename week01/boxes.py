import math
items = int(input("Enter the number of items: "))
items_per_box = int(input("Enter the number of items per box: "))

boxes = math.ceil(items/items_per_box)

print(f"For {items}, packing {items_per_box} in each box, ")
print(f"you will need {boxes} boxes")