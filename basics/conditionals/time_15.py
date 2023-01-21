hour=int(input())
minute=int(input())
hour_to_mins=hour*60
total_mins=hour_to_mins+minute+15
output_hour=total_mins//60
output_mins=total_mins % 60
if output_mins < 10:
    if output_hour <= 23:
        print(f'{output_hour}:0{output_mins}')
    else:
        print(f'0:0{output_mins}')
else:
    if output_hour <= 23:
        print(f'{output_hour}:{output_mins}')
    else:
        print(f'0:{output_mins}')
