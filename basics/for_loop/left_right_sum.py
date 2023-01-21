n1 = int(input())

first = []
second = []

for i in range(n1):
    number = int(input())
    first.append(number)

for i in range(n1):
    number = int(input())
    second.append(number)

if sum(first) == sum(second):
    print(f"Yes, sum = {sum(first)}")
else:
    print(f"No, diff = {abs(sum(first) - sum(second))}")
