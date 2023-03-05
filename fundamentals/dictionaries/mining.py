resources_list = []
resources = {}

while True:
    str_input = input()
    if str_input == "stop":
        break
    resources_list.append(str_input)

for i in range(0, len(resources_list), 2):
    resource = resources_list[i]
    quantity = int(resources_list[i + 1])

    resource_exists = resources.get(resource, False)
    if resource_exists is False:
        resources[resource] = quantity
    else:
        resources[resource] += quantity

for key, value in resources.items():
    print(f"{key} -> {value}")
