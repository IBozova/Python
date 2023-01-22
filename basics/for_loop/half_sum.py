from sys import maxsize

n = int(input())
total = 0
n_max = -maxsize

for i in range(n):
    n2 = int(input())
    if n2 > n_max:
        n_max = n2
    total += n2

total_sum = total - n_max
if total_sum == n_max:
    print("Yes")
    print(f"Sum = {abs(total_sum)}")
else:
    print("No")
    print(f"Diff = {abs(total_sum-n_max)}")
