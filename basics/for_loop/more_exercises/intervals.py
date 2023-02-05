turns = int(input())

total_points = 0
row_1 = 0
row_2 = 0
row_3 = 0
row_4 = 0
row_5 = 0
row_6 = 0

for i in range(turns):
    number = int(input())
    if 0 <= number <= 9:
        total_points += number * 0.2
        row_1 += 1
    elif 10 <= number <= 19:
        total_points += number * 0.3
        row_2 += 1
    elif 20 <= number <= 29:
        total_points += number * 0.4
        row_3 += 1
    elif 30 <= number <= 39:
        total_points += 50
        row_4 += 1
    elif 40 <= number <= 50:
        total_points += 100
        row_5 += 1
    else:
        total_points /= 2
        row_6 += 1

print(f"{total_points:.2f}")
print(f"From 0 to 9: {(row_1/turns)*100:.2f}%")
print(f"From 10 to 19: {(row_2/turns)*100:.2f}%")
print(f"From 20 to 29: {(row_3/turns)*100:.2f}%")
print(f"From 30 to 39: {(row_4/turns)*100:.2f}%")
print(f"From 40 to 50: {(row_5/turns)*100:.2f}%")
print(f"Invalid numbers: {(row_6/turns)*100:.2f}%")
