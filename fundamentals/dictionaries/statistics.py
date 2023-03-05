command = input()

stats = {}

while True:
    if command == "statistics":
        break
    key, value = command.split(": ")
    key_exists = stats.get(key, False)

    if key_exists:
        stats[key] += int(value)
    else:
        stats[key] = int(value)

    command = input()

print("Products in stock:")
for key, value in stats.items():
    print(f"- {key}: {value}")
# [print(f"- {key}: {value}") for key, value in stats.items()]
print(f"Total Products: {len(stats.keys())}")
print(f"Total Quantity: {sum(stats.values())}")
