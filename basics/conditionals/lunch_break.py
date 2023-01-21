from math import ceil

series_name = input()
episode_time = int(input())
break_time = int(input())

watch_time = break_time - (break_time / 8 + break_time / 4)
if watch_time >= episode_time:
    print(
        f"You have enough time to watch {series_name} and left with {ceil(watch_time - episode_time)} minutes free time."
    )
else:
    print(
        f"You don't have enough time to watch {series_name}, you need {ceil(abs(watch_time - episode_time))} more minutes."
    )
