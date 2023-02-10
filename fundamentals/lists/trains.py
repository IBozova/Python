wagons = int(input())

train_list = [0 for _ in range(wagons)]

data = input()

while True:
    if data == "End":
        break

    command = data.split(" ")[0]

    if command == "add":
        people = int(data.split(" ")[1])
        train_list[-1] += people
    else:
        index = int(data.split(" ")[1])
        people = int(data.split(" ")[2])
        if command == "insert":
            train_list[index] += people
        elif command == "leave":
            train_list[index] -= people

    data = input()

print(train_list)
