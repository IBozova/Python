items = [i.lower() for i in input().split(" ")]

word_dict = {key: items.count(key) for key in items}

filtered_dict = dict(filter(lambda x: x[1] % 2 != 0, word_dict.items()))

print(" ".join(filtered_dict.keys()))
