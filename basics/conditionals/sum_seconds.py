import math

time_first = int(input())
time_second = int(input())
time_third = int(input())
team_total = time_first + time_second + time_third
minutes = team_total / 60
minutes = math.floor(minutes)
seconds = team_total % 60
if seconds < 10:
    print(f"{minutes}:0{seconds}")
else:
    print(f"{minutes}:{seconds}")
