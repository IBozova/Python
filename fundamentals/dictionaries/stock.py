data = input().split(" ")
stock = {data[i]: int(data[i + 1]) for i in range(0, len(data), 2)}

search_products = input().split(" ")

for item in search_products:

    item_in_dict = stock.get(item, False)

    if item_in_dict:
        print(f"We have {item_in_dict} of {item} left")
    else:
        print(f"Sorry, we don't have {item}")

    # if item in stock.keys():
    #     print(f"We have {stock[item]} of {item} left")
    # else:
    #     print(f"Sorry, we don't have {item}")
