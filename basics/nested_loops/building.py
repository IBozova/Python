floors = int(input())
rooms = int(input())

result = []

for floor in range(floors, 0, -1):
    for room in range(rooms):
        if floor == floors:
            result.append(f"L{floor}{room}")
        elif floor % 2 == 0:
            result.append(f"O{floor}{room}")
        elif floor % 2 != 0:
            result.append(f"A{floor}{room}")
    print(" ".join(result))
    result.clear()
