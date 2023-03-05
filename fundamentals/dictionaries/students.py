command = input()

my_dict = {}

while True:
    # if len(command.split(":")) == 1:
    #     break
    if ":" not in command:
        break

    name, student_id, course = command.split(":")
    course = course.lower()

    course_exists = my_dict.get(course, False)

    if course_exists:
        my_dict[course] += [name, student_id]
    else:
        my_dict[course] = [name, student_id]

    command = input()


if "_" in command:
    command = " ".join(command.split("_"))

for key, value in my_dict.items():
    if key == command:
        for i in range(0, len(value), 2):
            print(f"{value[i]} - {value[i + 1]}")
