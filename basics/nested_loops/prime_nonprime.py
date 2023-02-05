sum_prime = 0
sum_non_prime = 0

while True:
    number = input()
    if number == "stop":
        break
    number = int(number)
    if number < 0:
        print("Number is negative.")
        continue
    while True:
        if number == 0 or number == 1:
            break
        elif number % 2 == 0 or number % 3 == 0 or number % 5 == 0 or number % 7 == 0:
            if number == 2 or number == 3 or number == 5 or number == 7:
                sum_prime += number
            else:
                sum_non_prime += number
        else:
            sum_prime += number
        break


print(f"Sum of all prime numbers is: {sum_prime}")
print(f"Sum of all non prime numbers is: {sum_non_prime}")
