person = {'first_name':'Asabeneh','last_name':'Yetayeh','age':250,'country':'Finlandia','is_marred':True,
          'skills':['JavaScript','React','Nodo','MongoDB','Python'],'dirección':{'calle':'Espacio calle','código postal':'02210'}}

print("Point 01\n",person['skills'])
print("Point 02")
if person['skills']:
    check='Python' in person['skills']
    print(check)
print("Point 03")
if 'JavaScript' and 'React' in person['skills']:
    