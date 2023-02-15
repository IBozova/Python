str_input = input()
list_input = [int(i) for i in str_input]

even_list = list(filter(lambda x: (x % 2 == 0), list_input))
odd_list = list(filter(lambda y: (y % 2 != 0), list_input))

even_sum = sum(even_list)
odd_sum = sum(odd_list)

print(f"Odd sum = {odd_sum}, Even sum = {even_sum}")
