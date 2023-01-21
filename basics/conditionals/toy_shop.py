vacation_price = float(input())
puzzles = int(input())
dolls = int(input())
bears = int(input())
minions = int(input())
trucks = int(input())

count = puzzles + dolls + bears + minions + trucks
toys = puzzles * 2.6 + dolls * 3 + bears * 4.1 + minions * 8.2 + trucks * 2
total = 0
greater_than_50 = count >= 50  # True | False

if greater_than_50:
    total = (toys * 0.75) * 0.9
else:
    total = toys * 0.9

is_enough = total >= vacation_price

if is_enough:
    print(f"Yes! {(total - vacation_price):.2f} lv left.")
else:
    print(f"Not enough money! {abs(total - vacation_price):.2f} lv needed.")
