countries = input().split(", ")
capitals = input().split(", ")

# 1
# for i in range(len(countries)):
#     print(f"{countries[i]} -> {capitals[i]}")

# 2
# capitals_dict = {countries[i]: capitals[i] for i in range(len(countries))}

# for key, value in capitals_dict.items():
#     print(f"{key} -> {value}")

# 3
capitals_dict = dict(zip(countries, capitals))

for key, value in capitals_dict.items():
    print(f"{key} -> {value}")
