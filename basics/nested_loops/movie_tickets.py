student_tickets = 0
standart_tickets = 0
kid_tickets = 0

while True:
    movie = input()
    if movie == "Finish":
        break
    capacity = int(input())
    movie_total = 0
    while True:
        type_of_ticket = input()
        if type_of_ticket == "End":
            break
        elif type_of_ticket == "student":
            student_tickets += 1
        elif type_of_ticket == "standard":
            standart_tickets += 1
        else:
            kid_tickets += 1
        movie_total += 1
        full_seats = (movie_total / capacity) * 100
        if movie_total == capacity:
            break
    print(f"{movie} - {full_seats:.2f}% full.")

total_tickets = student_tickets + standart_tickets + kid_tickets

print(f"Total tickets: {total_tickets}")
print(f"{(student_tickets/total_tickets)*100:.2f}% student tickets.")
print(f"{standart_tickets/total_tickets*100:.2f}% standard tickets.")
print(f"{kid_tickets/total_tickets*100:.2f}% kids tickets.")
