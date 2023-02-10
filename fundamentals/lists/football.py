cards = input().split(" ")

team_a = 11
team_b = 11
team_list = []

set_cards = set(cards)

for item in set_cards:
    team_list.append(item.split("-")[0])

for team in team_list:
    if team == "A":
        team_a -= 1
    elif team == "B":
        team_b -= 1
    if team_a < 7 or team_b < 7:
        break

if team_a >= 7 and team_b >= 7:
    print(f"Team A - {team_a}; Team B - {team_b}")
else:
    print(f"Team A - {team_a}; Team B - {team_b}")
    print(f"Game was terminated")
