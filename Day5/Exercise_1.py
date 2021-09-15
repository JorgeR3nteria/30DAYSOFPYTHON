list=[]
l1=["Yugi","Joey","Bakura","Tea","Seto Kaiba"]
e=0
print("Point 1\n",list)
print("Point 2\n",l1)
print("Point 3\n",l1.__len__())
print("Point 4\n""The first element is: ",l1[0],"\nThe middle element is: ",l1[2],"\nThe ultimate element is: ",l1[-1])
#Point 5
mixed_data_types=["Jorge Renteria",23,1.72,"Soltero","Calle 90n #100-52"]
#Point 6
it_companies=["Facebook" , "Google" , "Microsoft" , "Apple" , "IBM" , "Oracle" ,"Amazon"]
print("Point 7\n",it_companies)
print("Point 8\n",it_companies.__len__())
print("Point 9\n""First element is:",it_companies[0],"\nMiddle element is:",len(it_companies)//2,"\nUltimate element is:",it_companies[-1])
it_companies[3]="Whatsapp"
print("Point 10\n",it_companies)
it_companies.append("Cisco")
print("Point 11\n",it_companies)
it_companies.insert(len(it_companies)//2,"uber")
print("Point 12\n",it_companies)
it_companies[1]=it_companies[1].upper()
print("Point 13\n",it_companies)
it_companies.append("#")
print("Point 14\n",it_companies)
print("Point 15")
if "Whatsapp" in it_companies:
    print("Yes, the company is listed")
else:
    print("No, the company is not on the list.")
it_companies.sort()
print("Point 16\n",it_companies)    
it_companies.reverse()
print("Point 17\n",it_companies)
#Data of the points 26 and 27
front_end=[ 'HTML' , 'CSS' , 'JS' , 'React' , 'Redux' ]
back_end=[ 'Node' , 'Express' , 'MongoDB' ]
join=front_end+back_end
print("Point 27")
join.insert(-3,"Python")
join.insert(-4,"Sql")
print(join)

