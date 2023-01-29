jury = int(input())

overall_mark = 0
count_marks = 0

while True:
    presentation = input()
    if presentation == "Finish":
        break
    presentation_avg = 0
    for i in range(1, jury + 1):
        mark = float(input())
        presentation_avg += mark
        overall_mark += mark
        count_marks += 1
    print(f"{presentation} - {presentation_avg/jury:.2f}.")

print(f"Student's final assessment is {overall_mark/count_marks:.2f}.")
