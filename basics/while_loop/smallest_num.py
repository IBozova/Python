from sys import maxsize

cmd = input()

smallest = maxsize

while True:
    if cmd == "Stop":
        break
    number = int(cmd)
    if number < smallest:
        smallest = number

    cmd = input()

print(smallest)
