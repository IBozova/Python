vacation_price = float(input())
money = float(input())

total_movement = money
spend_movm = 0
count_movm = 0

while True:
    type_movement = input()
    money_flow = float(input())

    if type_movement == "spend":
        spend_movm += 1
        count_movm += 1
        if total_movement <= money_flow:
            total_movement = 0
        else:
            total_movement -= money_flow
        if spend_movm == 5:
            print(f"You can't save the money.")
            print(count_movm)
            break
    elif type_movement == "save":
        spend_movm = 0
        count_movm += 1
        total_movement += money_flow
        if total_movement >= vacation_price:
            print(f"You saved the money for {count_movm} days.")
            break
