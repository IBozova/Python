number_bottles = int(input())

detergent = number_bottles * 750
plates = 0
pots = 0
count_loading = 0
enough = True

while True:
    dishes = input()
    if dishes == "End":
        break
    elif dishes != "End":
        count_loading += 1
        dishes = int(dishes)
        if count_loading % 3 == 0:
            pots += dishes * 15
        elif count_loading % 3 != 0:
            plates += dishes * 5
    if plates + pots > detergent:
        enough = False
        break

if enough is True:
    print("Detergent was enough!")
    print(f"{plates/5:.0f} dishes and {pots/15:.0f} pots were washed.")
    print(f"Leftover detergent {detergent-(plates+pots)} ml.")
else:
    print(f"Not enough detergent, {abs((pots+plates)-detergent)} ml. more necessary!")
