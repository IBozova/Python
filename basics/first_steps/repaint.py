naylon_sqm=int(input())
paint_liters=int(input())
diluent_liters=int(input())
hours=int(input())
materials_total=((naylon_sqm+2)*1.5)+((paint_liters*1.1)*14.5)+(diluent_liters*5)+0.4
labour_total=(materials_total*0.3)*hours
total=materials_total+labour_total
print(total)
