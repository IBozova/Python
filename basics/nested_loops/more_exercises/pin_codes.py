number_1 = int(input())
number_2 = int(input())
number_3 = int(input())

for i in range(1, number_1 + 1):
    if i % 2 == 0:
        for j in range(1, number_2 + 1):
            if j == 2 or j == 3 or j == 5 or j == 7:
                for k in range(1, number_3 + 1):
                    if k % 2 == 0:
                        print(i, j, k)
                    else:
                        continue
            else:
                continue
    else:
        continue
