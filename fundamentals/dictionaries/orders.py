"""
while loop;  input within the while; stop when command buy; X
add input with split by space to dict; X
quantity & price to product, parsed to int/float respectively X

list within dict 
dict = {key: [quantity, price]}

check if key exists (get); X
if exists
    increase quantity X
    if price is different
        replace price X

print all dict items with total price
for key, value in quantities_dict.items():
    print(key -> value[0] * value[1])

"""

orders_dict = {}

while True:
    product_input = input()
    if product_input == "buy":
        break
    else:
        products_list = product_input.split(" ")
        for i in range(0, len(products_list), 3):
            product = products_list[i]
            price = float(products_list[i + 1])
            quantity = int(products_list[i + 2])
            product_in = orders_dict.get(product, False)
            if product_in is False:
                orders_dict[product] = [price, quantity]
            else:
                orders_dict[product][1] += quantity
                if orders_dict[product][0] != price:
                    orders_dict[product][0] = price

for key, value in orders_dict.items():
    print(f"{key} -> {value[0] * value[1]:.2f}")
