#2D list = a list of lists

drink = ["Coffe", "soda", "tea"]
dinner = ["Pizza", "hamburger", "hotdog"]
dessert = ["cake", "ice cream"]

food = [drink, dinner, dessert]

print(food[0])
print(food[0][1])
print(food[0][2])
drink.append( "pepsi")

for i in drink:
    print(i)


