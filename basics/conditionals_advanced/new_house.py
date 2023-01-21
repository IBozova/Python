flower = input()
flower_count = int(input())
flower_budget = int(input())
total = 0
if flower == "Roses" and flower_count > 80:
    total = (flower_count * 5) * 0.9
elif flower == "Roses":
    total = flower_count * 5
elif flower == "Dahlias" and flower_count > 90:
    total = (flower_count * 3.8) * 0.85
elif flower == "Dahlias":
    total = flower_count * 3.8
elif flower == "Tulips" and flower_count > 80:
    total = (flower_count * 2.8) * 0.85
elif flower == "Tulips":
    total = flower_count * 2.8
elif flower == "Narcissus" and flower_count < 120:
    total = (flower_count * 3) * 1.15
elif flower == "Narcissus":
    total = flower_count * 3
elif flower == "Gladiolus" and flower_count < 80:
    total = (flower_count * 2.5) * 1.2
else:
    total = flower_count * 2.5
if flower_budget >= total:
    print(
        f"Hey, you have a great garden with {flower_count} {flower} and {(flower_budget - total):.2f} leva left."
    )
else:
    print(f"Not enough money, you need {abs(flower_budget - total):.2f} leva more.")
