name = input()

GRADES = 12
sum_marks = 0
grade = 1
fail = 0

while True:
    mark = float(input())
    if mark >= 4:
        sum_marks += mark
        grade += 1
    else:
        fail += 1
    if fail == 2:
        print(f"{name} has been excluded at {grade} grade")
        break
    if grade > GRADES:
        break

if fail != 2:
    print(f"{name} graduated. Average grade: {sum_marks/GRADES:.2f}")
