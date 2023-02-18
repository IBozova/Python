class Party:
    people: list = []


command = input()

my_party = Party()

while True:
    if command == "End":
        break

    my_party.people.append(command)
    command = input()

print(f"Going: {', '.join(my_party.people)}")
print(f"Total: {len(my_party.people)}")
