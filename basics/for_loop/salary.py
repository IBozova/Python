tabs = int(input())
salary = int(input())

site_dict = {"Facebook": 150, "Instagram": 100, "Reddit": 50}

for i in range(tabs):
    site = input()
    if site in site_dict.keys():
        salary -= site_dict[site]
        if salary <= 0:
            print("You have lost your salary.")
            break

if salary > 0:
    print(salary)
