money_string = input().split(", ")
beggars = int(input())

money_list = [int(money) for money in money_string]

beggars_list = [0 for _ in range(beggars)]
index = 0

for money in money_list:
    beggars_list[index] += money
    index += 1
    if index == beggars:
        index = 0

# money_list = money_list[::-1]

# while money_list:
#     for index in range(len(beggars_list)):
#         beggars_list[index] += money_list[-1]
#         money_list.pop()
#         if bool(money_list) is False:
#             break


print(beggars_list)
