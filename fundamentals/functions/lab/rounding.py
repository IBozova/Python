def rounding(floating):
    return round(floating, 0)


string_num = input().split(" ")
float_num = [float(num) for num in string_num]
output = [int(rounding(i)) for i in float_num]


print(output)
