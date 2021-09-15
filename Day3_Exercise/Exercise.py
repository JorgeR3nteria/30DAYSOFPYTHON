from math import dist
#Dia 3: 30 días de programación en Python
#Punto 1 al 3
age=int(23)
height=float(1.72)
com=14+5j
print("Point 4")
Base=int(input("Type a number for the base: "))
Height=int(input("Type a number for the height: "))
Area=0.5
#Operations
Total= Area*Base*Height
print("Its result is:",Total)
print("Point 5")
#Data Input
side_a=int(input("Type a number for side a:"))
side_b=int(input("Type a number for side b:"))
side_c=int(input("Type a number for side c:"))
#Operations
perimeter=side_a+side_b+side_c
#Output
print("Its parameter is: ",perimeter)
print("Point 6")
#Data Input
length=int(input("Enter the length of the rectangle: "))
width=int(input("Enter the width of the rectangle: "))
#Operations
area=length*width
Perimeter=2*(length+width)
#Output
print("The total area of the rectangle is ",area,"and the perimeter is:",Perimeter)
print("Point 7")
#Data Input
pi=3.14
radius=float(input("Enter a number for the radius: "))
#Result
Area=pi*(radius**2)
c=2*pi*radius
#Output
print("The area of the radius ",Area,"and the cirfumference is",c)
'''print("Point 8")
pending=2
intersection_xy=2/2
intersection_y=-2'''
print("Point 9")
#Data Input
#hallar la pendiente de m=y2-y1/x2-x1
y2,y1=2,3
x2,x1=4,2
#Operations
m=y2-y1/x2-x1
#Hallar la distancia euclidiana
punto_a=(2,2)
punto_b=(6,10)
Distancia =dist(punto_a,punto_b)
#Output
print("Euclidean distance is",Distancia,"and The slope is:",m)
#Data Input
v1,v2= 'Python','dragon'
print("Point 12\n""Its length is equal:",v1==v2)
print("Point 13")
if "on" in v1 and v2:
    print("Yes, if found in both values")
else:
    print("No, the word was not found")
print("Point 14")
#Data
Phrase="Espero que este curso no esté lleno de jerga"
#Output
if "jerga" in Phrase:
    print("If it's in the phrase")
else:
    print("Not found in the phrase")
print("Point 15\n","not found in the words 'on' python and dragon?")
if "on" in v1 and v2:
    print("False, if found in the 2 words")
else:
    print("True, the word is not found")
print("Point 16\n""convert the 'python' word to decimals and then to string", str(float(len("python"))))
#Data
op1,op2=9.8,10
#Output
print("Point 20\n""Is it the same?",op1==op2)
print("Point 21")
#Operations
User_Hours=int(input("Please, enter the number of hours worked: "))
Hourly_rate=int(input("Please, enter an hourly rate number: "))
operation=round(User_Hours*Hourly_rate)
#Output
print(operation)
print("Point 22")
#Data
Año, day, hour, minutes= 365, 31, 60, 60
#Informatión
cant=int(input("Enter your current age:"))
#Operations
V=int(cant*Año*day*hour*minutes)
print("Your have lived for",V,"Seconds")
