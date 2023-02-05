charity_sum = int(input())

cash_transaction = 0
card_transaction = 0
count_cash = 0
count_card = 0
transaction_count = 0
raised_sum = False

while True:
    payment = input()
    if payment == "End":
        break
    else:
        payment = int(payment)
        transaction_count += 1
        if transaction_count % 2 == 0:
            if payment < 10:
                print("Error in transaction!")
            else:
                card_transaction += payment
                count_card += 1
                print("Product sold!")
        else:
            if payment > 100:
                print("Error in transaction!")
            else:
                cash_transaction += payment
                count_cash += 1
                print("Product sold!")
        if cash_transaction + card_transaction >= charity_sum:
            raised_sum = True
            break

if raised_sum is True:
    print(f"Average CS: {cash_transaction/count_cash:.2f}")
    print(f"Average CC: {card_transaction/count_card:.2f}")
else:
    print("Failed to collect required money for charity.")
