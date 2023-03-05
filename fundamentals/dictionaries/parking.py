"""
input for num of commands;
for loop with range of num_commands with input.split by " "
if split_list[0] == "register"
split_list[1] & split_list[2] into a dict
split.dict.get to check if name exists
>error
>add to dict
if split_list[0] =="unregister"
> if name exists > pop
>error
print key, value
"""
num_commands = int(input())
parking_dict = {}

for i in range(num_commands):
    data = input().split(" ")
    command = data[0]
    name = data[1]
    if command == "register":
        plate_num = data[2]
        spot_in = parking_dict.get(name, False)
        if spot_in is False:
            parking_dict[name] = plate_num
            print(f"{name} registered {plate_num} successfully")
        else:
            print(f"ERROR: already registered with plate number {plate_num}")
    elif command == "unregister":
        if name in parking_dict.keys():
            print(f"{name} unregistered successfully")
            parking_dict.pop(name)
        else:
            print(f"ERROR: user {name} not found")

for key, value in parking_dict.items():
    print(f"{key} => {value}")
