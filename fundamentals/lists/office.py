happiness = [int(i) for i in input().split(" ")]
factor = int(input())

count_happy = 0

multiplied = list(map(lambda happy: happy * factor, happiness))
average = sum(multiplied) / len(multiplied)

for number in multiplied:
    if number >= average:
        count_happy += 1

if count_happy >= len(happiness) / 2:
    print(f"Score: {count_happy}/{len(happiness)}. Employees are happy!")
else:
    print(f"Score: {count_happy}/{len(happiness)}. Employees are not happy!")
