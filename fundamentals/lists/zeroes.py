number_list = [int(num) for num in input().split(", ")]

over_zero = [numb for numb in number_list if numb != 0]
zero_only = [zero for zero in number_list if zero == 0]

sorted_list = over_zero + zero_only

print(sorted_list)

## solution 2

number_list.sort(key=lambda number: 1 if number != 0 else 0, reverse=True)

print(number_list)
