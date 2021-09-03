#Día 2: 30 días de programación en Python
#Ejercicio: Nivel 1
f_n , l_n="Jorge","Renteria" #f_n -> primer nombre y l_n -> Apellido
full_name='Jorge Renteria'
country='Colombia'
city='Cali'
age=23
year=2021
is_married=False
is_true=True
is_light_on=False
day,mounth,year= 2,8,2021
#Ejercicio: Nivel 2
print('1. Checking data types using type')
print("the datatype for",f_n,"is:",type(f_n))
print("the datatype for",l_n,"is:",type(l_n))
print("the datatype for",full_name,"is:",type(full_name))
print("the datatype for",country,"is:",type(country))
print("the datatype for",city,"is:",type(city))
print("the datatype for",age,"is:",type(age))
print("the datatype for",year,"is:",type(year))
print("the datatype for",is_married,"is:",type(is_married))
print("the datatype for",is_true,"is:",type(is_true))
print("the datatype for",is_light_on,"is:",type(is_light_on))
print("the datatype for",day,"is:",type(day))
print("the datatype for",mounth,"is:",type(mounth))
print("the datatype for",year,"is:",type(year))
print("2. Function len")
print("The length of the name is:",f_n.__len__())
print("3. Length comparison")
print("The length of name and last_name is equals?:",(f_n.__len__ == l_n.__len__))
print("4. Arithmetic Operations")
num_one=5
num_two=4
#Operaciones
total=num_one+num_two
diff=num_two-num_one
product=num_two*num_one
division=num_one/ num_two
remainder=num_two%num_one
exp=num_one** num_two
floor_division=num_one//num_two
#Output
print("Me atrevi a poner el resultado de este punto.")
print("1.Total sum:",total)
print("2.Total subtraction ",diff)
print("3.Total of multiplication:",product)
print("4.Total of division:",division)
print("5.The remainder of the division is:",remainder)
print("6.Total power is:",exp)
print("7.Total of floor_division:",floor_division)
print("5. Calculate the radius")
circle=int(30)
area_of_circle=3.14*(circle**2)
circum_of_circle=2*3.14*circle
print("The area of te circle is:",area_of_circle)
print("circumference is:",circum_of_circle)
print("User Radius")
radius=float(input("Type a number for the radio:"))
area=3.14*(radius**2)
print(area)
print("6. Input function")
name=str(input("Write your name:"))
last_name=str(input("Write your last_name:"))
Country=str(input("Write the country of birth:"))
Age=int(input("Please, enter your age:"))
print("My name is",name,last_name,"i am from",Country,"and i have",Age,"years old")
