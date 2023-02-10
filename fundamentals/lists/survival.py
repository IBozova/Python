string_list = input().split(" ")
pop_number = int(input())

number_list = [int(num) for num in string_list]
list_popped = number_list.copy()
list_popped_count = len(list_popped)
number_list_count = len(number_list) - pop_number

for number in number_list:
    if list_popped_count == number_list_count:
        break
    else:
        list_popped.remove(min(list_popped))
        list_popped_count -= 1

print(list_popped)
