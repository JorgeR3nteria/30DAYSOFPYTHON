'''Día 9: 30 días de programación en Python'''
Age=int(input('Enter your age:'))
print('Point 01')
if Age > 18:
    print("Old enough to drive")
elif Age <=18:
    subtract= 18-(Age)
    print("You need",subtract,"more years to learn to drive")
print('Point 02')
my_age=int(input('Enter your age:'))
your_age=int(input('Enter your age:'))
d1= my_age - your_age
d2= your_age - my_age
if my_age > your_age:
    print("I am older by",d1,"years")
elif my_age==your_age:
    print("We are the same age")
else:
    print("You're older than me by",d2,"years")
print('Point 03')
User_1=int(input('Enter a number for A:'))
User_2=int(input('Enter a number for B:'))
if User_1 > User_2:
    print(User_1,"is greater than",User_2)
elif User_1 == User_2:
    print(User_1,"equals",User_2)
else:
    print(User_1,"is less than",User_2)


