count_words = int(input())

syn_dict = {}

for i in range(count_words):
    word = input()
    synonym = input()

    key_exists = syn_dict.get(word, False)

    # if key_exists is False:
    #     syn_dict[word] = []
    # syn_dict[word].append(synonym)

    if key_exists:
        syn_dict[word].append(synonym)
    else:
        syn_dict[word] = [synonym]


for key, value in syn_dict.items():
    print(f"{key} - {', '.join(value)}")
