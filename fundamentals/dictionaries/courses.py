"""
courses_dict = {}
while_loop with courses_input
if input == end -->break
else:
courses_list = courses_input.split(" : ")
course = courses_list[0]
student = courses_list[1]
course_in = courses_dict.get()
if course_in is False:
>add course = [student]
else:
>course[1] += student

for key, value in courses_dict.items:
    print key count(value)
    for name in names
    print 
"""
courses_dict = {}

while True:
    courses_input = input()
    if courses_input == "end":
        break
    else:
        courses_list = courses_input.split(" : ")
        course = courses_list[0]
        student = courses_list[1]
        course_in = courses_dict.get(course, False)
        if course_in is False:
            courses_dict[course] = [student]
        else:
            courses_dict[course].append(student)

for key, value in courses_dict.items():
    print(f"{key}: {len(value)}")
    for name in value:
        print(f"-- {name}")
