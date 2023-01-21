points = int(input())
if points <= 100:
    bonus_points = 5
elif 100 <= points <= 1000:
    bonus_points = points * 0.2
elif points >= 1000:
    bonus_points = points * 0.1
if points % 2 == 0:
    total_bonus = bonus_points + 1
elif points % 5 == 0:
    total_bonus = bonus_points + 2
else:
    total_bonus = bonus_points
total_points = points + total_bonus
print(total_bonus, end="\n")
print(total_points)
