film_budget = float(input())
crew = int(input())
crew_clothing = float(input())

decor = film_budget * 0.1
total = 0

if crew > 150:
    crew_clothing *= 0.9

total = crew_clothing * crew + decor

if film_budget >= total:
    print(f"Action!")
    print(f"Wingard starts filming with {(film_budget - total):.2f} leva left.")
else:
    print(f"Not enough money!")
    print(f"Wingard needs {(total - film_budget):.2f} leva more.")
