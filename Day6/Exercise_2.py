t_B=("David R","Omar E","Juan B","Julian C","Juan R")
t_S=("Monica","Mabel","Laura","Patricia")
brothers=t_B+t_S
family_members=brothers+("Walter R","Martha H")
print("Point 1")
print(family_members[-2:])
print(family_members[0:-2])
print("Point 2")
Fruits=('Lemon','Naranja','Avocado','Coco','Raspberry')
Vegetables=('Carrot','Lettuce','Beets','Asparagus')
Prod_Anim=('Bed','Toys','Comb','Food bowl','Towel')
food_stuff_tp=(Fruits+Vegetables+Prod_Anim)
print(food_stuff_tp)
print("Point 3")
food_stuff_lt=list(food_stuff_tp)
print(food_stuff_lt)
print("Point 4")
split=len(food_stuff_lt)//2
print(split)
print("Point 5")
print(food_stuff_lt[:3])
print(food_stuff_lt[-3:])
#Point 6
del food_stuff_tp
print("Point 7")
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
if "Estonia" in nordic_countries:
    print("Yes,if it's a nordic country")
else:
    print("No, it's not a nordic country")
if "Iceland" in nordic_countries:
    print("Yes,if it's a nordic country")
else:
    print("No, it's not a nordic country")