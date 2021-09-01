from math import dist
print('Este es el punto 2')
# arithmetic operations 
addition=int(2+3)
subtraction=int(3-1)
multiplication=int(2*3)
division=int(3/2)
exponential=int(3**2)
waste=int(3%2)
en_div=int(3//2)
#Output
print("the sum is:",addition)
print("subtraction is:",subtraction)
print("multiplication is:",multiplication)
print("division is:",division)
print ("your waste is: ",waste)
print ("The entire division is: ",en_div) 
print('Este es el punto 3')
#Cadenas
name=str("jorge iván")
ln=str("renteria hernández")
Country=str("colombia")
msg=str("Estoy disfrutando de 30 dias de python")
#Output
print("Mi name is: ", name.title())
print("Mi last name is: ",ln.title())
print("Mi country of birth is",Country.capitalize())
print("Your message is: ",msg)
print('Este es el punto 4')
print(type(int(10)))
print(type(float(9.8)))
print(type(complex(1 + 3j)))
print(type([1, 2, 3])is list)
print(type({'name':'Asabeneh'})is dict)
print(type(set({9.8, 3.14, 2.7})))
print(type(tuple((9.8, 3.14, 2.7))))
print('Exercise:level 3')
#Datos para resolver el punto 1 del ejercicio:nivel 3
c=4
a=18
com=9+8j
l=["123456","10581276","Go"]
t=("hola","mundo",1,9,41,50)
phrase=str("Aprendiendo python con FrontendCafe")
total=int(a*c)
dec=float(c/a)
conjunto=set()
conjunto={5,9,4,0,"Hola","FrontendCafe",9.51}
dictionary={"Hola":"Hello","Azul":"Blue","Amarillo":"yellow"}
#Output
print(total) #Este es un Entero
print(dec) #Este es un float
print(com,type(com)is complex) #Este es un complejo
print(phrase) #Este es un string
print(a!=c) #Este es un booleano
print("Esto es una lista: ",l)
print("Esto es una tupla: ", t)
print(conjunto)
print(dictionary)
#Este es el punto 2 del ejercicio:nivel 3
print("Punto 2 - Ejercicio: nivel 3")
punto_1=(2,3)
punto_2=(10,8)

distancia=dist(punto_1,punto_2)
print(distancia)