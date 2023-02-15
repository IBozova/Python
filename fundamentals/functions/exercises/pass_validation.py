def check_length(string: str):
    if len(string) >= 6 and len(string) <= 10:
        return True
    return False


def all_chars_valid(string: str):
    for letter in string:
        if not letter.isalnum():
            return False
    return True


def has_two_digits(string: str):
    count = 0
    for letter in string:
        if letter.isdigit():
            count += 1
        if count == 2:
            return True
    return False


password_str = input()
length_valid = check_length(password_str)
chars_valid = all_chars_valid(password_str)
two_digits = has_two_digits(password_str)

if length_valid is False:
    print("Password must be between 6 and 10 characters")
if chars_valid is False:
    print("Password must consist only of letters and digits")
if two_digits is False:
    print("Password must have at least 2 digits")

if all([length_valid, chars_valid, two_digits]):
    print("Password is valid")
