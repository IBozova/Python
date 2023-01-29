first = int(input())
second = int(input())
num = int(input())

iteration = 0
found = False
x = 0
y = 0

for i in range(first, second + 1):
    for j in range(first, second + 1):
        iteration += 1
        if i + j == num:
            x = i
            y = j
            found = True
            break
    if found:
        break

if found:
    print(f"Combination N:{iteration} ({x} + {y} = {num})")
else:
    print(f"{iteration} combinations - neither equals {num}")
