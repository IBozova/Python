text = input()

text_dict = {}

if " " in text:
    multi_text = text.split(" ")
    text_str = "".join(multi_text)
    for i in text_str:
        if i not in text_dict:
            text_dict[i] = text.count(i)
else:
    for i in text:
        if i not in text_dict:
            text_dict[i] = text.count(i)

for key, value in text_dict.items():
    print(f"{key} -> {value}")
