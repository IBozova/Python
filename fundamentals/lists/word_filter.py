words = input().split(" ")

filtered_words = list(filter(lambda x: len(x) % 2 == 0, words))

print(filtered_words)
