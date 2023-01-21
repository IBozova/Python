basketball_fee = int(input())
trainers = basketball_fee - (basketball_fee * 0.4)
clothes = trainers - (trainers * 0.2)
ball = clothes * 0.25
accessories = ball * 0.2
basketball_total = basketball_fee + trainers + clothes + ball + accessories
print(basketball_total)
