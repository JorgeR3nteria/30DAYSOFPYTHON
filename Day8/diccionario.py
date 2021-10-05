'''Día 8: 30 días de programación en Python'''
perro={}
print("Point 01\n",perro)
#Point 02
perro={"Dog1":{"Name":"Firulais","Color":"Cafe","Race":"Labrador","Legs":"4","Age":"3"},
"Dog2":{"Name":"Mario","Color":"Blanco","Race":"Pastor Aleman","Legs":"4","Age":"5"},
"Dog3":{"Namee":"Ximena","Color":"Crema","Race":"Poodle","Legs":"4","Age":"2"}}
#Point 03
Students={"Name":"Jorge","Apellido":"Cifuentes","Genero":"Masculino","Edad":"23","Est_Civil":"Soltero","Habilidades":["Paciencia"],"Pais":"Argentina","Ciudad":"Buenos Aires"}
print('Point 04\n',len(Students))
print('Point 05')
print(Students.get("Habilidades"))
print(type(Students["Habilidades"]))
Students['Habilidades']='Creatividad','Adaptibilidad'
print('Point 06\n',Students)
key=[key for key in Students]
print('Point 07\n',key)
valor=Students.values()
print('Point 08\n',valor)
print('Point 09\n',Students.items())
Students.pop("Habilidades")
print('Point 10\n',Students)
#Point 11
del perro