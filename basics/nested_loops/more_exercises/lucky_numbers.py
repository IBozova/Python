number = int(input())

lucky_numbers = []

for i in range(1111, 10000):
    number_string = str(i)

    first = int(number_string[0])
    second = int(number_string[1])
    third = int(number_string[2])
    fourth = int(number_string[3])

    if all([first, second, third, fourth]):
        if first + second == third + fourth:
            if number % (first + second) == 0:
                lucky_numbers.append(i)

print(*lucky_numbers, sep=" ")


number = int(input())

for i in range(1, 10):
    for o in range(1, 10):
        for p in range(1, 10):
            for l in range(1, 10):
                if i + o == p + l and number % (i + o) == 0:
                    print(f"{i}{o}{p}{l}", end=" ")
