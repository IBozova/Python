inheritance = float(input())
year_death = int(input())

odd_living_years = 0
even_living_years = 0


for i in range(1800, year_death + 1):
    if i % 2 == 0:
        even_living_years += 12000
    elif i % 2 != 0:
        odd_living_years += ((18 + (i - 1800)) * 50) + 12000

if inheritance < odd_living_years + even_living_years:
    print(
        f"He will need {(odd_living_years+even_living_years)-inheritance:.2f} dollars to survive."
    )
else:
    print(
        f"Yes! He will live a carefree life and will have {inheritance-(odd_living_years+even_living_years):.2f} dollars left."
    )
