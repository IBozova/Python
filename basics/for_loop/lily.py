n = int(input())
washer_price = float(input())
price_toys = int(input())

total = 0

for i in range(1, n + 1):
    if i % 2 == 0:
        total += 10 * (i / 2) - 1
    else:
        total += price_toys

if total >= washer_price:
    print(f"Yes! {total-washer_price:.2f}")
else:
    print(f"No! {abs(total-washer_price):.2f}")
