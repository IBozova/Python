contact_list = []
number_input = 0
phonebook = {}


while True:
    contact_input = input()
    if "-" not in contact_input:
        number_input += int(contact_input)
        break
    else:
        contact = contact_input.split("-")
        contact_list.append(contact)

contact_list2 = [item for innerlist in contact_list for item in innerlist]

for x in range(0, len(contact_list2), 2):
    name = contact_list2[x]
    phone_num = contact_list2[x + 1]
    num_in = phonebook.get(name, False)
    if num_in is False:
        phonebook[name] = phone_num
    else:
        phonebook.update(name=phone_num)

for i in range(number_input):
    name = input()
    name_exists = phonebook.get(name, False)
    if name_exists:
        print(f"{name} -> {phonebook[name]}")
    else:
        print(f"Contact {name} does not exist.")


# for key, value in phonebook.items():
#     if key in name_list:
#         print(f"{key} -> {value}")
#     else:
#         name_filter = list(filter(lambda x: x not in phonebook.keys(), name_list))
#         for i in name_filter:
#             print(f"Contact {i} does not exist.")
