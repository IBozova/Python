def palindrome(string: str):
    if string == string[::-1]:
        return True
    else:
        return False


num_list = [i for i in input().split(", ")]

for y in num_list:
    print(palindrome(y))
