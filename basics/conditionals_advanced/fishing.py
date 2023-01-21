fishing_budget = int(input())
season = input()
fisher_count = int(input())
total = 0
if season == "Spring" and fisher_count <= 6:
    total = 3000 * 0.9
elif season == "Spring" and 7 <= fisher_count <= 11:
    total = 3000 * 0.85
elif season == "Spring" and fisher_count >= 12:
    total = 3000 * 0.75
elif (season == "Summer" or season == "Autumn") and fisher_count <= 6:
    total = 4200 * 0.9
elif (season == "Summer" or season == "Autumn") and 7 <= fisher_count <= 11:
    total = 4200 * 0.85
elif (season == "Summer" or season == "Autumn") and fisher_count >= 12:
    total = 4200 * 0.75
elif season == "Winter" and fisher_count <= 6:
    total = 2600 * 0.9
elif season == "Winter" and 7 <= fisher_count <= 11:
    total = 2600 * 0.85
elif season == "Winter" and fisher_count >= 12:
    total = 2600 * 0.75
if season != "Autumn" and fisher_count % 2 == 0:
    total *= 0.95
if fishing_budget >= total:
    print(f"Yes! You have {(fishing_budget - total):.2f} leva left.")
else:
    print(f"Not enough money! You need {(total-fishing_budget):.2f} leva.")


# fishing_budget = int(input())
# season = input()
# fisher_count = int(input())
# total = 0

# seasonDict: dict = {"Spring": 3000, "Summer": 4200, "Autumn": 4200, "Winter": 2600}

# total = seasonDict[season]

# if fisher_count <= 6:
#     total *= 0.9
# elif 7 <= fisher_count <= 11:
#     total *= 0.85
# else:
#     total *= 0.75

# if season != "Autumn" and fisher_count % 2 == 0:
#     total *= 0.95

# if fishing_budget >= total:
#     print(f"Yes! You have {(fishing_budget - total):.2f} leva left.")
# else:
#     print(f"Not enough money! You need {(total-fishing_budget):.2f} leva.")
