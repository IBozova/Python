word = input()

sum_letters = 0

for letter in word:
    if letter == "a":
        sum_letters += 1
    elif letter == "e":
        sum_letters += 2
    elif letter == "i":
        sum_letters += 3
    elif letter == "o":
        sum_letters += 4
    elif letter == "u":
        sum_letters += 5

print(sum_letters)
