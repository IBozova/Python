def factorial(num):
    multiplied = num
    for i in range(1, num):
        multiplied *= i

    return multiplied


number_1 = int(input())
number_2 = int(input())

factorial_1 = factorial(number_1)
factorial_2 = factorial(number_2)

print(f"{factorial_1 / factorial_2:.2f}")
