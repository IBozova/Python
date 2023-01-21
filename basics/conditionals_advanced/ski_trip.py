days = int(input())
accomodation = input()
review = input()
room_dict: dict = {
    "room for one person": 18,
    "apartment": 25,
    "president apartment": 35,
}
nights = days - 1
total = 0

if nights < 10 and accomodation == "apartment":
    total = room_dict["apartment"] * 0.7
elif 10 <= nights <= 15 and accomodation == "apartment":
    total = room_dict["apartment"] * 0.65
elif nights > 15 and accomodation == "apartment":
    total = room_dict["apartment"] * 0.5
elif nights < 10 and accomodation == "president apartment":
    total = room_dict["apartment"] * 0.9
elif 10 <= nights <= 15 and accomodation == "president apartment":
    total = room_dict["apartment"] * 0.85
elif nights > 15 and accomodation == "president apartment":
    total = room_dict["president apartment"] * 0.8
elif accomodation == "room for one person":
    total = room_dict["room for one person"]

if review == "positive":
    total = total * nights * 1.25
else:
    total = total * nights * 0.9
print(f"{(total):.2f}")
