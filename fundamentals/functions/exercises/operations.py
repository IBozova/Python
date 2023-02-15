def sum_numbers(x, y):
    return x + y


def subtract(i, k):
    return i - k


a = int(input())
b = int(input())
c = int(input())

sum_num = sum_numbers(a, b)
sub_num = subtract(sum_num, c)

print(sub_num)
