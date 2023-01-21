month = input()
nights = int(input())

studio_dict: dict = {
    "May": 50,
    "October": 50,
    "June": 75.2,
    "September": 75.2,
    "July": 76,
    "August": 76,
}
apt_dict: dict = {
    "May": 65,
    "October": 65,
    "June": 68.7,
    "September": 68.7,
    "July": 77,
    "August": 77,
}

total_studio = 0
total_apt = 0

if nights > 14 and (month == "May" or month == "October"):
    total_studio = studio_dict[month] * 0.7
elif nights > 7 and (month == "May" or month == "October"):
    total_studio = studio_dict[month] * 0.95
elif nights > 14 and (month == "June" or month == "September"):
    total_studio = studio_dict[month] * 0.8
else:
    total_studio = studio_dict[month]
if nights > 14:
    total_apt = apt_dict[month] * 0.9
else:
    total_apt = apt_dict[month]

print(f"Apartment: {(total_apt * nights):.2f} lv.")
print(f"Studio: {(total_studio * nights):.2f} lv.")
