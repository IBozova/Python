num = int(input())

count = 0

for i in range(num + 1):
    for j in range(num + 1):
        for k in range(num + 1):
            if i + j + k == num:
                count += 1

print(count)
