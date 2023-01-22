username = input()
correct_password = input()

while True:
    user_input = input()
    if correct_password == user_input:
        print(f"Welcome {username}!")
        break
