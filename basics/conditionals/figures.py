shape = input()
if shape == "square":
    sq_side_1 = float(input())
    print(round((sq_side_1 * sq_side_1), 3))
elif shape == "rectangle":
    rec_side_1 = float(input())
    rec_side_2 = float(input())
    print(round((rec_side_1 * rec_side_2), 3))
elif shape == "circle":
    radius = float(input())
    print(round((radius * radius * 3.14159265359), 3))
else:
    tri_side_1 = float(input())
    tri_side_2 = float(input())
    print(round(((tri_side_1 * tri_side_2) / 2), 3))
