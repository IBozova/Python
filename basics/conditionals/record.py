record_secs = float(input())
meters = float(input())
sec_per_m = float(input())

resistance_secs = (meters // 15) * 12.5
swimming_time = (sec_per_m * meters) + resistance_secs

if swimming_time >= record_secs:
    print(f"No, he failed! He was {(swimming_time - record_secs):.2f} seconds slower.")
else:
    print(f"Yes, he succeeded! The new world record is {(swimming_time):.2f} seconds.")

budget = float(input())
video_cards = int(input())
processors = int(input())
ram = int(input())
total_parts = (
    (video_cards * 250)
    + (((video_cards * 250) * 0.35) * processors)
    + (((video_cards * 250) * 0.1) * ram)
)
total_sum = 0
if video_cards > processors:
    total_sum = total_parts * 0.85
else:
    total_sum = total_parts
if budget >= total_sum:
    print(f"You have {(budget - total_sum):.2f} leva left!")
else:
    print(f"Not enough money! You need {(total_sum-budget):.2f} leva more!")
