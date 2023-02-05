months = int(input())

electricity_total = 0
others = 0

for i in range(months):
    electricity = float(input())
    electricity_total += electricity
    others += (electricity + 35) * 0.2

total_bills = (months * 20) + (months * 15) + electricity_total + others
bills = (months * 20) + (months * 15) + electricity_total
print(f"Electricity: {electricity_total:.2f} lv")
print(f"Water: {months*20:.2f} lv")
print(f"Internet: {months*15:.2f} lv")
print(f"Other: {total_bills:.2f} lv")
print(f"Average: {(total_bills+bills)/months:.2f} lv")
