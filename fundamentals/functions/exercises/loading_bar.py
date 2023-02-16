loaded = int(input())

loaded_list = []

for i in range(10, 110, 10):
    if i <= loaded:
        loaded_list.append("%")
    else:
        loaded_list.append(".")

loaded_str = "".join(loaded_list)

if loaded < 100:
    print(f"{loaded}% [{loaded_str}]")
    print("Still loading...")
else:
    print(f"{loaded}% Complete!")
    print(f"[{loaded_str}]")
