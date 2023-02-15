def tab(item: str, count_item: int):
    if item == "coffee":
        return count_item * 1.5
    elif item == "water":
        return count_item * 1
    elif item == "coke":
        return count_item * 1.4
    else:
        return count_item * 2


order = input()
count = int(input())

bill = tab(order, count)
print(f"{bill:.2f}")
