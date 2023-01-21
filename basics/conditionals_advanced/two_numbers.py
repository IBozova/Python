N1 = int(input())
N2 = int(input())
symbol = input()
total = 0
type_of_number = ""


if symbol == "%":
    if N2 == 0:
        total = 0
    else:
        total = N1 % N2
elif symbol == "-":
    total = N1 - N2
elif symbol == "*":
    total = N1 * N2
elif symbol == "/":
    if N2 == 0:
        total = 0
    else:
        total = N1 / N2
else:
    total = N1 + N2
if (symbol == "+" or symbol == "-" or symbol == "*") and (total % 2 == 0):
    type_of_number = "even"
else:
    type_of_number = "odd"

if symbol == "/" and N2 != 0:
    print(f"{N1} {symbol} {N2} = {(total):.2f}")
elif symbol == "%" and N2 != 0:
    print(f"{N1} {symbol} {N2} = {(total)}")
elif (symbol == "/" or symbol == "%") and (N2 == 0):
    print(f"Cannot divide {N1} by zero")
else:
    print(f"{N1} {symbol} {N2} = {(total)} - {type_of_number}")
