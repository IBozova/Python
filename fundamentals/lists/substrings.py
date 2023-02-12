line_1 = input().split(", ")
line_2 = input().split(", ")

found_words = set()

for words in line_2:
    for word in line_1:
        if word in words:
            found_words.add(word)
            break

list_words = list(found_words)
print(list_words)
