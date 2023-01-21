lenght = int(input())
width = int(input())
height = int(input())
procent = float(input())
volume_liters = (lenght * width * height) / 1000
filledup_space = procent / 100
liters_needed = volume_liters * (1 - filledup_space)
print(liters_needed)
