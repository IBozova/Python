transports = int(input())

van_tonnage = 0
truck_tonnage = 0
train_tonnage = 0

for i in range(transports):
    tonnage = int(input())
    if tonnage >= 12:
        train_tonnage += tonnage
    elif 4 <= tonnage <= 11:
        truck_tonnage += tonnage
    else:
        van_tonnage += tonnage

total_price = van_tonnage * 200 + truck_tonnage * 175 + train_tonnage * 120
total_tonnage = van_tonnage + truck_tonnage + train_tonnage

print(f"{total_price/total_tonnage:.2f}")
print(f"{(van_tonnage/total_tonnage)*100:.2f}%")
print(f"{(truck_tonnage/total_tonnage)*100:.2f}%")
print(f"{(train_tonnage/total_tonnage)*100:.2f}%")
