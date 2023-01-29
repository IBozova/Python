change = float(input())

count_coins = 0
returned_change = int(change * 100)

# while True:
#     if returned_change >= 200:
#         count_coins += returned_change // 200
#         returned_change -= count_coins * 200
#         if returned_change == 0:
#             print(count_coins)
#             break
#     elif returned_change >= 100:
#         count_coins += 1
#         returned_change -= 100
#         if returned_change == 0:
#             print(count_coins)
#             break
#     elif returned_change >= 50:
#         count_coins += 1
#         returned_change -= 50
#         if returned_change == 0:
#             print(count_coins)
#             break
#     elif returned_change >= 20:
#         count_coins += returned_change // 20
#         returned_change -= (returned_change // 20) * 20
#         if returned_change == 0:
#             print(count_coins)
#             break
#     elif returned_change >= 10:
#         count_coins += 1
#         returned_change -= 10
#         if returned_change == 0:
#             print(count_coins)
#             break
#     elif returned_change >= 5:
#         count_coins += 1
#         returned_change -= 5
#         if returned_change == 0:
#             print(count_coins)
#             break
#     elif returned_change >= 2:
#         count_coins += returned_change // 2
#         returned_change -= (returned_change // 2) * 2
#         if returned_change == 0:
#             print(count_coins)
#             break
#     elif returned_change == 1:
#         count_coins += 1
#         returned_change -= 1
#         if returned_change == 0:
#             print(count_coins)
#             break


coin_list = [200, 100, 50, 20, 10, 5, 2, 1]

for coin in coin_list:
    while True:
        count_coins += returned_change // coin
        returned_change -= coin * (returned_change // coin)
        if returned_change < coin:
            break

print(count_coins)
