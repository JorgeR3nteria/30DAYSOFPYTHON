'''Día 2: 30 días de programación en Python
Exercise: Level 1'''
#Point 03 and 04
name,last_name='Jorge','Renteria'
#Point 05
full_name='Jorge Renteria'
#Point 06 and 07
country,city='Colombia','Cali'
#Point 08 and 09
age,year=23,2021
#Point 10
is_married=False
#Point 11
is_true=True
#Point 12
is_light_on=False
#Point 13
Day,Mounth,Year=24,'September',2021
'''Exercise: Level 2'''
print("Point 01")
print(type(name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))
print(type(Day))
print(type(Mounth))
print(type(Year))
print("Point 02")
print(len(name))
print("Point 03")
print(len(name)==len(last_name))
#Point 04
num_one=5
num_two=4
#Operations
total=num_one+num_two
diff=num_two-num_one
product=num_two*num_one
division=num_one/num_two
remainder=num_two%num_one
exp=num_one** num_two
floor_division=num_one//num_two
print("Point 4.1:",total)
print("Point 4.2:",diff)
print("Point 4.3:",product)
print("Point 4.4:",division)
print("Point 4.5:",remainder)
print("Point 4.6:",exp)
print("Point 4.7:",floor_division)
#Point 05
pi=3.1416
radius_circle=30
user_radius=int(input("enter a number for the radio:"))
#Operations
area_of_circle=pi*radius_circle**2
circum_of_circle=2*pi*radius_circle
area_circle_user=pi*user_radius**2
print("Point 5.1:",area_of_circle)
print("Point 5.2:",circum_of_circle)
print("Point 5.3:",area_circle_user)
print("Point 06")
Name=input('Please, enter your first name: ')
Last_name=input('Please, enter your last name: ')
Country=input('Please, enter your country of residence: ')
City=input('Please, enter the city where you live: ')
Age=input('Please, enter your age: ')
print("My name is",Name,Last_name,"i live in the city of",City,"located in the country of",Country,"and i have",Age,"old years")