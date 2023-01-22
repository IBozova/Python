group_count = int(input())

group_1 = 0
group_2 = 0
group_3 = 0
group_4 = 0
group_5 = 0

for i in range(group_count):
    people_count = int(input())
    if people_count <= 5:
        group_1 += people_count
    elif 6 <= people_count <= 12:
        group_2 += people_count
    elif 13 <= people_count <= 25:
        group_3 += people_count
    elif 26 <= people_count <= 40:
        group_4 += people_count
    else:
        group_5 += people_count
total_count = group_1 + group_2 + group_3 + group_4 + group_5

print(f"{(group_1/total_count)*100:.2f}%")
print(f"{(group_2/total_count)*100:.2f}%")
print(f"{(group_3/total_count)*100:.2f}%")
print(f"{(group_4/total_count)*100:.2f}%")
print(f"{(group_5/total_count)*100:.2f}%")
