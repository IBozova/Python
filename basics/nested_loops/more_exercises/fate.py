men = int(input())
women = int(input())
tables = int(input())

taken_tables = 0
stop = False

for i in range(1, men + 1):
    for j in range(1, women + 1):
        taken_tables += 1
        if taken_tables <= tables:
            print(f"({i} <-> {j})", end=" ")
        else:
            stop = True
            break
    if stop:
        break
