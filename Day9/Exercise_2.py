print("Point 01")
ratings=int(input('Tell us what your score was:'))
if ratings >=0 and ratings<=49:
    print('F')
elif ratings>=50 and ratings<=59:
    print('D')
elif ratings>=60 and ratings<=69:
    print('C')
elif ratings>=70 and ratings<=79:
    print('B')
else:
    print('A')
print("Point 02")
def Seasons_years(mes):
    if mes in ('diciembre','enero','febrero'):
        print('Invierno')
    elif mes in ('marzo','abril','mayo'):
        print('Primavera')
    elif mes in ('junio','julio','agosto'):
        print('Verano')
    else:
        print('Otoño')
mes=input('Enter a month:')
Seasons_years(mes)
print("Point 03")
fruit_list=['banana','orange','mango','lemon']
fruit=str(input('Write a fruit: '))
if fruit in fruit_list:
    print('This fruit already exists in the list')
else:
    fruit_list.append(fruit)
    print('No such fruit found, added to the list')
