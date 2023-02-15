def grading(mark: float):
    if mark < 3:
        return "Fail"
    elif 3 <= mark <= 3.49:
        return "Poor"
    elif 3.50 <= mark <= 4.49:
        return "Good"
    elif 4.50 <= mark <= 5.49:
        return "Very Good"
    else:
        return "Excellent"


mark_input = float(input())
# mark_int = int(mark_input * 100)

grading_result = grading(mark_input)

print(grading_result)
