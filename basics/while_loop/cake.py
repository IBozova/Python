length_cake = int(input())
width_cake = int(input())

size_cake = length_cake * width_cake
leftover = size_cake
cake_piece = 0

while True:

    if cake_piece == "STOP":
        if leftover == size_cake:
            print(f"{size_cake} pieces are left.")
            break
        elif leftover != size_cake:
            print(f"{leftover} pieces are left.")
            break
    elif cake_piece != "STOP":
        cake_piece = int(cake_piece)
        if leftover >= cake_piece:
            leftover -= cake_piece
        else:
            print(
                f"No more cake left! You need {abs(leftover-cake_piece)} pieces more."
            )
            break
        cake_piece = input()
