def operations(num_operation, num_a, num_b):
    if num_operation == "multiply":
        return num_a * num_b
    elif num_operation == "divide":
        return int(num_a / num_b)
    elif num_operation == "add":
        return num_a + num_b
    else:
        return num_a - num_b


operation = input()
a = int(input())
b = int(input())

operation_result = operations(operation, a, b)
print(operation_result)
