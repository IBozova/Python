fail_grades = int(input())

sum_grades = 0
count_grades = 0
fail_tasks = 0
last_problem = ""

while True:
    name_task = input()
    if name_task == "Enough":
        print(f"Average score: {sum_grades/count_grades:.2f}")
        print(f"Number of problems: {count_grades}")
        print(f"Last problem: {last_problem}")
        break
    last_problem = name_task
    task_grade = int(input())
    if task_grade <= 4:
        fail_tasks += 1
        sum_grades += task_grade
        count_grades += 1
        if fail_tasks == fail_grades:
            sum_grades += task_grade
            count_grades += 1
            print(f"You need a break, {fail_grades} poor grades.")
            break
    else:
        sum_grades += task_grade
        count_grades += 1
