n = int(input())

total_1 = 0
total_2 = 0
total_3 = 0
total_4 = 0
total_5 = 0

for i in range(n):
    n2 = int(input())
    if 1 <= n2 < 200:
        total_1 += 1
    elif 200 <= n2 <= 399:
        total_2 += 1
    elif 400 <= n2 <= 599:
        total_3 += 1
    elif 600 <= n2 <= 799:
        total_4 += 1
    else:
        total_5 += 1

print(f"{(total_1/n)*100:.2f}%")
print(f"{(total_2/n)*100:.2f}%")
print(f"{(total_3/n)*100:.2f}%")
print(f"{(total_4/n)*100:.2f}%")
print(f"{(total_5/n)*100:.2f}%")

# n = int(input())

# totals = [0, 0, 0, 0, 0]

# for i in range(n):
#     n2 = int(input())
#     if 1 <= n2 < 200:
#         totals[0] += 1
#     elif 200 <= n2 <= 399:
#         totals[1] += 1
#     elif 400 <= n2 <= 599:
#         totals[2] += 1
#     elif 600 <= n2 <= 799:
#         totals[3] += 1
#     else:
#         totals[4] += 1

# for i in range(len(totals)):
#     print(f"{((totals[i] / n) * 100):.2f}%")
