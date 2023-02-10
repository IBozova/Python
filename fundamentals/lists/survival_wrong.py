string_list = input().split(" ")
pop_number = int(input())

number_list = [int(num) for num in string_list]

number_list.sort(reverse=True)

list_popped = number_list[: len(number_list) - pop_number]

print(list_popped)
