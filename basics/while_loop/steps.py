steps_total = 0

while True:
    steps = input()
    if steps == "Going home":
        steps_total += int(input())
        break
    elif steps != "Going home":
        steps_total += int(steps)
        if steps_total >= 10000:
            break

if steps_total >= 10000:
    print(f"Goal reached! Good job!")
    print(f"{steps_total-10000} steps over the goal!")
else:
    print(f"{abs(steps_total-10000)} more steps to reach goal.")
