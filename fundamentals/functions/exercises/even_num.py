str_list = [int(i) for i in input().split(" ")]

even_list = list(filter(lambda x: (x % 2 == 0), str_list))

print(even_list)
