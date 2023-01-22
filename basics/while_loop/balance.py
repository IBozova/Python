installment = input()

sum_money = 0

while True:
    if installment == "NoMoreMoney":
        break

    number = float(installment)
    if number < 0:
        print("Invalid operation!")
        break

    sum_money += number
    print(f"Increase: {number:.2f}")

    installment = input()

print(f"Total: {sum_money:.2f}")
