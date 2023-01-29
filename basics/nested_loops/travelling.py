destination = input()
needed_money = float(input())

saved_money = 0

while True:
    while True:
        saved_money += float(input())
        if saved_money >= needed_money:
            saved_money = 0
            print(f"Going to {destination}!")
            break
    destination = input()
    if destination == "End":
        break
    needed_money = float(input())
