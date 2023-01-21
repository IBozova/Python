exam_hour = int(input())
exam_minute = int(input())
arrival_hour = int(input())
arrival_minute = int(input())

arrival_minutes = arrival_hour * 60 + arrival_minute
exam_minutes = exam_hour * 60 + exam_minute
difference = exam_minutes - arrival_minutes
difference_hour = difference // 60
difference_mins = difference % 60
difference_hour2 = difference * -1 // 60

if difference == 0:
    print(f"On time")
elif 1 <= difference <= 30:
    print(f"On time")
    print(f"{exam_minutes-arrival_minutes} minutes before the start")
elif 30 < difference <= 59:
    print(f"Early")
    print(f"{exam_minutes-arrival_minutes} minutes before the start")
elif difference >= 60:
    if difference_mins < 10:
        print(f"Early")
        print(f"{difference_hour}:0{difference_mins} hours before the start")
    else:
        print(f"Early")
        print(f"{difference_hour}:{difference_mins} hours before the start")
elif -59 <= difference <= -1:
    print(f"Late")
    print(f"{abs(exam_minutes-arrival_minutes)} minutes after the start")
else:
    if -10 <= difference_mins <= -1:
        print(f"Late")
        print(f"{abs(difference_hour2)}:0{abs(difference_mins)} hours after the start")
    else:
        print(f"Late")
        print(f"{abs(difference_hour2)}:{abs(difference_mins)} hours after the start")
