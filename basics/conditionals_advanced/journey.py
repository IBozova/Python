destination_budget = float(input())
season = input()
total = 0
destination = ""
accomodation = ""

accomodationDict: dict = {"Summer": "Camp", "Summer": "Hotel", "Winter": "Hotel"}

if season == "summer" and destination_budget <= 100:
    total = destination_budget * 0.3
elif season == "winter" and destination_budget <= 100:
    total = destination_budget * 0.7
elif season == "summer" and destination_budget <= 1000:
    total = destination_budget * 0.4
elif season == "winter" and destination_budget <= 1000:
    total = destination_budget * 0.8
else:
    total = destination_budget * 0.9
if destination_budget <= 100:
    destination = "Bulgaria"
elif destination_budget <= 1000:
    destination = "Balkans"
else:
    destination = "Europe"
if destination_budget <= 100:
    destination = "Bulgaria"
elif destination_budget <= 1000:
    destination = "Balkans"
else:
    destination = "Europe"

if season == "summer" and destination == "Bulgaria":
    accomodation = "Camp"
elif season == "winter" and destination == "Bulgaria":
    accomodation = "Hotel"
elif season == "summer" and destination == "Balkans":
    accomodation = "Camp"
elif season == "winter" and destination == "Balkans":
    accomodation = "Hotel"
else:
    accomodation = "Hotel"

if destination_budget <= 100:
    print(f"Somewhere in {destination}")
    print(f"{accomodation} - {(total):.2f}")
elif destination_budget <= 1000:
    print(f"Somewhere in {destination}")
    print(f"{accomodation} - {(total):.2f}")
else:
    print(f"Somewhere in {destination}")
    print(f"{accomodation} - {(total):.2f}")
