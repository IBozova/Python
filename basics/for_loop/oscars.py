actor = input()
academy_points = float(input())
count_jury = int(input())

points = academy_points

for i in range(count_jury):
    name_jury = input()
    jury_points = float(input())
    points += len(name_jury) * jury_points / 2
    if points > 1250.5:
        print(
            f"Congratulations, {actor} got a nominee for leading role with {points:.1f}!"
        )
        break

if points <= 1250.5:
    print(f"Sorry, {actor} you need {1250.5-points:.1f} more!")
