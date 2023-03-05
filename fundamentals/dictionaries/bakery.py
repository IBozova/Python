# food_items = input().split(" ")

# bakery = {}

# for i in range(0, len(food_items), 2):
#     bakery[food_items[i]] = food_items[i + 1]

# print(bakery)

food_items = input().split(" ")
bakery = {food_items[i]: int(food_items[i + 1]) for i in range(0, len(food_items), 2)}
print(bakery)
