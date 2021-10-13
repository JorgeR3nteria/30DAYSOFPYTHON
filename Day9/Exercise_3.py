person = {'first_name':'Asabeneh','last_name':'Yetayeh','age':250,'country':'Finland','is_marred':True,
          'skills':['JavaScript','React','Node','MongoDB','Python'],'dirección':{'calle':'Espacio calle','código postal':'02210'}}
print("Point 01")
for k, v in person.items():
    if k == 'skills':
        middle=len(v)//2
        print(v[middle])
print("Point 02")
if person['skills']:
    for k in person['skills']:
        if k == 'Python':
            print(k)
print("Point 03")
message = ''
for k, v in person.items():
    if k == 'skills':
        for index in range(len(v)):
            print(v[index], end=" ")
            if v == ['JavaScript', 'React', 'Node', 'MongoDB', 'Python']:
                message = 'He is a fullstack developer'
            elif v == ['Node', 'MongoDB', 'Python']:
                message = 'He is a back end developer'
            elif v == ['JavaScript', 'React']:
                message = 'He is a front end developer'
        print(message)
print("Point 04")
message = ''
if person['is_marred'] and person['country'] == 'Finland':
    print(f"{person['first_name']}"\
        , f"{person['last_name']}"\
        , f"lives in {person['country']}."\
        , "He is married.")
else:
    print('This not found.')
