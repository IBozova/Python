number = int(input())

divisors = []

for i in range(1, number + 1):
    if number % i == 0:
        divisors.append(i)

sum_divisors = sum(divisors)

if sum_divisors / 2 == number:
    print("We have a perfect number!")
else:
    print("It's not so perfect.")
