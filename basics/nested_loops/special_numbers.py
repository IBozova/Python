number = int(input())

special_numbers = []

for i in range(1111, 10000):
    count = 0
    for num in str(i):
        if int(num) == 0:
            break
        elif number % int(num) == 0:
            count += 1
    if count == 4:
        special_numbers.append(str(i))

print(" ".join(special_numbers))

# number = int(input())

# special_numbers = []

# for i in range(1111, 10000):
#     if all([num for num in str(i)]) is not False:
#         if len([num for num in str(i) if number % int(num) == 0]) == 4:
#             special_numbers.append(str(i))

# print(**special_numbers, sep=" ")
