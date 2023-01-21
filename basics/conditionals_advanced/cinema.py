type_of_screening = input()
rows = int(input())
columns = int(input())
theater_capacity = rows * columns
if type_of_screening == "Premiere":
    print(f"{(theater_capacity*12):.2f} leva")
elif type_of_screening == "Normal":
    print(f"{(theater_capacity*7.5):.2f} leva")
else:
    print(f"{(theater_capacity*5):.2f} leva")
