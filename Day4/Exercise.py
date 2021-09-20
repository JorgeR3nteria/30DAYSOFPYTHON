#Dia 4: 30 días de programación en Python
print("Point 1\n"'Treinta'+" "+'dias'+" "+'de'+" "+'Python')
print("Point 2\n"'Codificación'+" "+'para'+" "+'todos')
empresa="Codificación para todos"
print("Point 3 and 4\n",empresa)
print("Point 5\n""Su longitud es:",empresa.__len__())
print("Point 6\n",empresa.upper())
print("Point 7\n",empresa.lower())
print("Point 8")
print(empresa.capitalize())
print(empresa.title())
print(empresa.swapcase())
cut=empresa[-10:-1]
print("Point 9\n",cut)
search=empresa.find("Codificación")
print("Point 10\n""The coding word is found in the position:",search)
txt=empresa.replace("Codificación","Python")
print("Point 11\n""The new phrase is:",txt)
Txt="Python for Everyone"
new_txt=Txt.replace("Python for Everyone","Python for All")
print("Point 12\n",new_txt)
new=empresa.split(' ')
print("Point 13\n",new)
print("Point 14\n",'Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon'.split(","))
print("Point 15\n",empresa[0])
print("Point 16\n",empresa[22])
print("Point 17\n",empresa[10])
acronim_1="python for everyone"
acronim_2="coding for all"
def acronym(acronim_1):
    acronim_1=acronim_1.split()
    C=""
    for word in acronim_1:
        if word != "and":
            C += str(word[0])
    return C.upper()
def acronym(acronim_2):
    acronim_2=acronim_2.split()
    G=""
    for words in acronim_2:
        if words != "and":
            G += str(words[0])
    return G.upper()
result = acronym(acronim_1)
res=acronym(acronim_2)
print("Point 18\n",result)
print("Point 19\n",res)
index=empresa.index("C")
i=empresa.index("p")
print("Point 20\n",index)
print("Point 21\n",i)
sentence="Coding For All People".rfind("l")
print("Point 22\n",sentence)
Oracion='No puede terminar una oración con porque porque porque porque es una conjunción'
subcadena=""
print("Point 23\n",Oracion.find("porque"))
print("Point 24\n",Oracion.rindex("porque"))

