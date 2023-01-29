wanted_book = input()

checked_books = 0

while True:
    books = input()
    if books == "No More Books":
        print(f"The book you search is not here!")
        print(f"You checked {checked_books} books.")
        break
    if wanted_book == books:
        print(f"You checked {checked_books} books and found it.")
        break
    else:
        checked_books += 1
