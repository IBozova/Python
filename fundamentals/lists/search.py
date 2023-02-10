number = int(input())
word = input()

strings = []

for i in range(number):
    string = input()
    strings.append(string)

print(strings)
print(list(filter(lambda x: word in x, strings)))

# number = int(input())
# word = input()

# strings = []

# for i in range(number):
#     string = input()
#     strings.append(string)

# print(strings)

# filtered = []

# for string in strings:
#     if word in string:
#         filtered.append(string)

# print(filtered)
