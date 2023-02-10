numbers = [int(x) for x in input().split(", ")]
# numbers = list(map(int, input().split(", ")))

indexes = []

# # for index in range(len(numbers)):
# #     if numbers[index] % 2 == 0:
# #         indexes.append(index)


for index, number in enumerate(numbers):
    if number % 2 == 0:
        indexes.append(index)

print(indexes)
