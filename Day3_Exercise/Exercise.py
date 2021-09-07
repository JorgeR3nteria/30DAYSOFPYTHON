from math import dist
#Dia 3: 30 días de programación en Python
#Punto 1 al 3
age=int(23)
height=float(1.72)
com=14+5j
print("punto 4")
Base=int(input("Type a number for the base: "))
Height=int(input("Type a number for the height: "))
#Operations
Total= Base*Height/2
#Output
print(Total)
print("Punto 5")
#Data Input
side_a=int(input("Type a number for side a:"))
side_b=int(input("Type a number for side b:"))
side_c=int(input("Type a number for side c:"))
#Operations
perimeter=side_a+side_b+side_c
#Output
print(perimeter)
print("punto 6")
#Data Input
length=int(input("Enter the length of the rectangle: "))
width=int(input("Enter the width of the rectangle: "))
#Operations
area=length*width
Perimeter=2*(length+width)
#Output
print("The total area of the rectangle is:",area)
print("The perimeter of the rectangle is:",Perimeter)
print("Punto 7")
pi=3.14
radius=float(input("Enter a number for the radius: "))
#Result
Area=pi*(radius**2)
c=2*pi*radius
#Output
print("The area of the radius is:",Area)
print("The cirfumference of the radius is:",c)
print("punto 8")
pending=2
intersection_xy=2/2
intersection_y=-2
print("punto 9")
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
print("Euclidean distance is:",Distancia)
print("The slope is: ",m)
print("punto 21")
hours=int(input("Type the hours "))
