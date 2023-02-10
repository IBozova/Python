# def length_names(name): return len(name)

# lambda name: len(name)


# 3, 5, 3, 5, 6, 4
# Kim = 3, Marry = 5, Ali = 3, Teddy = 5, Monika = 6, John = 4
# Monika = 6, Marry = 5, Teddy = 5, John = 4, Ali = 3, Kim = 3


names = input().split(", ")
names.sort(key=lambda name: (-len(name), name))

print(names)
