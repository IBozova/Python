companies_dict = {}

while True:
    companies_input = input()
    if companies_input == "End":
        break
    else:
        companies_list = companies_input.split(" -> ")
        company = companies_list[0]
        ids = companies_list[1]
        company_in = companies_dict.get(company, False)
        if company_in is False:
            companies_dict[company] = [ids]
        else:
            employees = companies_dict[company]
            if ids not in employees:
                companies_dict[company].append(ids)

for key, value in companies_dict.items():
    print(key)
    for item in value:
        print(f"-- {item}")
