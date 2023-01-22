limit = int(input())

sum_numbers = 0

while True:
    number = int(input())
    sum_numbers += number
    if sum_numbers >= limit:
        break

print(sum_numbers)
