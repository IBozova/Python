students = int(input())

total_marks = 0
top = 0
good = 0
satisfactory = 0
fail = 0

for i in range(students):
    mark = float(input())
    total_marks += mark
    if mark >= 5:
        top += 1
    elif 4.00 <= mark <= 4.99:
        good += 1
    elif 3.00 <= mark <= 3.99:
        satisfactory += 1
    else:
        fail += 1

print(f"Top students: {(top/students)*100:.2f}%")
print(f"Between 4.00 and 4.99: {(good/students)*100:.2f}%")
print(f"Between 3.00 and 3.99: {(satisfactory/students)*100:.2f}%")
print(f"Fail: {(fail/students)*100:.2f}%")
print(f"Average: {(total_marks/students):.2f}")
