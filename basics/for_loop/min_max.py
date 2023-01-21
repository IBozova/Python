
from sys import maxsize

iterations = int(input())

max_num = -maxsize
min_num = maxsize

for i in range(iterations):
    number = int(input())
    if number > max_num:
        max_num = number
    if number < min_num:
        min_num = number

print(f"Max number: {max_num}")
print(f"Min number: {min_num}")