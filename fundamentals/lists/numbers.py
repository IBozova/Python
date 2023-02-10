number = int(input())

numbers_list = []

for i in range(number):
    data = int(input())
    numbers_list.append(data)

command = input()

filtered = []

if command == "even":
    filtered = [number for number in numbers_list if number % 2 == 0 or number == 0]
elif command == "odd":
    filtered = [number for number in numbers_list if number % 2 != 0]
elif command == "negative":
    fileted = list(filter(lambda x: x < 0, numbers_list))
elif command == "positive":
    filtered = [number for number in numbers_list if number >= 0]

print(filtered)
