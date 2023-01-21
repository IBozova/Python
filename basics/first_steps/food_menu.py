chicken_menu = int(input())
fish_menu = int(input())
vegetarian_menu = int(input())
order_total = (
    ((chicken_menu * 10.35) + (fish_menu * 12.40) + (vegetarian_menu * 8.15))
    + (((chicken_menu * 10.35) + (fish_menu * 12.40) + (vegetarian_menu * 8.15)) * 0.2)
    + 2.5
)
print(order_total)
