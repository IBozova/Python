string = input()

string_list = []

for i in string:
    string_list = string.split(" ")

opposite_list = [int(i) * -1 for i in string_list]

print(opposite_list)
