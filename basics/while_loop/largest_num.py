from sys import maxsize

cmd = input()

largest = -maxsize

while True:
    if cmd == "Stop":
        break
    number = int(cmd)
    if number > largest:
        largest = number

    cmd = input()

print(largest)
