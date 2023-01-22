from math import floor

events = int(input())
starting_points = int(input())

total_points = starting_points
win_ranking = 0

event_dict = {"W": 2000, "F": 1200, "SF": 720}

for i in range(events):
    ranking = input()
    if ranking in event_dict.keys():
        total_points += event_dict[ranking]
    if ranking == "W":
        win_ranking += 1

print(f"Final points: {total_points}")
print(f"Average points: {floor((total_points-starting_points)/events)}")
print(f"{(win_ranking/events)*100:.2f}%")
