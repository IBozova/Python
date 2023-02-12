numbers = input().split(" ")
message = [letter for letter in input()]

indexes = []

for number in numbers:
    sum_digits = sum([int(digit) for digit in number])
    indexes.append(sum_digits)

indexes = indexes[::-1]

result = ""

while True:
    if bool(indexes) is False:
        break
    target_index = indexes.pop() % len(message)
    # while True:
    #     if target_index <= len(message):
    #         break
    #     target_index -= len(message)

    for index, letter in enumerate(message):
        if index == target_index:
            result += letter
            message.pop(index)
            break

print(result)
