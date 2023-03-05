force_dict = {}

while True:
    force_input = input()
    if force_input == "Lumpawaroo":
        break
    else:
        values_list = [item for sublist in force_dict.values() for item in sublist]
        if "->" not in force_input:
            force_list = force_input.split(" | ")
            side = force_list[0]
            name = force_list[1]
            side_in = force_dict.get(side, False)
            if name not in values_list:
                if side_in is False:
                    force_dict[side] = [name]
                else:
                    force_dict[side].append(name)
        else:
            force_list = force_input.split(" -> ")
            side = force_list[1]
            name = force_list[0]
            side_in = force_dict.get(side, False)
            if name not in values_list:
                if side_in is False:
                    force_dict[side] = [name]
                    print(f"{name} joins the {side} side!")
                else:
                    force_dict[side].append(name)
                    print(f"{name} joins the {side} side!")
            else:
                for key, value in force_dict.items():
                    if name in value:
                        force_dict[key].remove(name)
                        force_dict[side].append(name)
                        print(f"{name} joins the {side} side!")
                        break

for key, value in force_dict.items():
    if len(value) > 0:
        print(f"Side: {key}, Members: {len(value)}")
        for name in value:
            print(f"! {name}")
