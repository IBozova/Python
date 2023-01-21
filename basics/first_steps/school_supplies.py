pen_packs = int(input())
marker_packs = int(input())
liters = int(input())
discount = float(input())
discounted_price = ((pen_packs * 5.8) + (marker_packs * 7.2) + (liters * 1.2)) - (
    ((pen_packs * 5.8) + (marker_packs * 7.2) + (liters * 1.2)) * (discount / 100)
)
print(discounted_price)
