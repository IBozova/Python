note = input()

all_notes = [0 for _ in range(10)]
importance_list = []

while True:
    if note == "End":
        break

    importance = int(note.split("-")[0]) - 1
    activity = note.split("-")[1]
    all_notes[importance] = activity

    note = input()

all_notes = [x for x in all_notes if x != 0]

print(all_notes)
