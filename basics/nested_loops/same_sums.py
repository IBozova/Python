num_1 = int(input())
num_2 = int(input())

summed_list = []

for i in range(num_1, num_2 + 1):
    parsed_num = str(i)
    sum_even = 0
    sum_odd = 0

    for index in range(len(parsed_num)):
        if index % 2 == 0:
            sum_even += int(parsed_num[index])
        else:
            sum_odd += int(parsed_num[index])

    if sum_even == sum_odd:
        summed_list.append(parsed_num)

print(" ".join(summed_list))

#####

num_1 = int(input())
num_2 = int(input())

summed_list = []

while True:
    parsed_num = str(num_1)
    sum_even = 0
    sum_odd = 0

    index = 0
    while True:
        if parsed_num[index] % 2 == 0:
            sum_even += int(parsed_num[index])
        else:
            sum_odd += int(parsed_num[index])
        index += 1
        if index == len(parsed_num):
            break

    if sum_even == sum_odd:
        summed_list.append(parsed_num)

    num_1 += 1
    if num_1 == num_2:
        break

print(" ".join(summed_list))
