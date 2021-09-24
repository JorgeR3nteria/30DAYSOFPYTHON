A={ 19 , 22 , 24 , 20 , 25 , 26 }
B={ 19 , 22 , 20 , 25 , 26 , 24 , 28 , 27 }
print("Point 01\n",A.union(B))
print("Point 02\n",A.intersection(B))
print("Point 03\n",A.issubset(B))
print("Point 04\n",A.issuperset(B))
print("Point 05")
print(A.union(B))
print(B.union(A))
print("Point 06\n",A.symmetric_difference(B))
#Point 07
del A 
del B