words: list[str] = input().split(" ")
palindrome: str = input()

# palindromes_list: list[str] = []

# for word in words:
#     if word == word[::-1]:
#         palindromes_list.append(word)

palindromes_list: list[str] = [word for word in words if word == word[::-1]]

print(palindromes_list)
print(f"Found palindrome {palindromes_list.count(palindrome)} times")
