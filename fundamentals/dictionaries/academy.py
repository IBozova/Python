"""
num_students = int(input())
marks_dict = {}
for loop (num_students):
student_name=input()
grade = float(input())
student_in = marks_dict.get()
if student_in is False:
>add student = [grade]
else:
>student.append(grade)

for key, value in courses_dict.items:
	
    print key count(value)
    for name in names
    print 

"""
num_students = int(input())

marks_dict = {}

for i in range(num_students):
    student_name = input()
    grade = float(input())
    student_in = marks_dict.get(student_name, False)
    if student_in is False:
        marks_dict[student_name] = [grade]
    else:
        marks_dict[student_name].append(grade)

for key, value in marks_dict.items():
    aveg = sum(value) / len(value)
    if aveg >= 4.5:
        print(f"{key} -> {aveg:.2f}")
