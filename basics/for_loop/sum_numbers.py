numbers = int(input())
sum_numbers = 0
numbers_list = []
found = False

for i in range(numbers):
    number = int(input())
    sum_numbers += number
    numbers_list.append(number)

for number in numbers_list:
    if number == sum(numbers_list) - number:
        print("Yes")
        print(f"Sum = {number}")
        found = True

if found is False:
    print("No")
    print(f"Diff = {abs(max(numbers_list) - (sum(numbers_list) - max(numbers_list)))}")
