number = int(input())

count = 1

for x in range(1, number + 1):
    for y in range(1, x + 1):
        if count > number:
            break
        print(count, end=" ")
        count += 1
    print("")
