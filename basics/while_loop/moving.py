height = int(input())
width = int(input())
lenght = int(input())

m3 = height * width * lenght
free_space = m3

while True:
    boxes = input()
    if boxes == "Done":
        print(f"{free_space} Cubic meters left.")
        break
    elif boxes != "Done":
        boxes = int(boxes)
        if free_space >= boxes:
            free_space -= boxes
        else:
            print(
                f"No more free space! You need {abs(free_space-boxes)} Cubic meters more."
            )
            break
