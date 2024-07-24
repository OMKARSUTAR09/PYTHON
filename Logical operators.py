#Logical operators
a = 50
b = 20

#for NOT operater 
#NOT operator coverts true into false and false into true
print("NOT operator : ", not (a == b))  
print("NOT operator : ", not (a > b))

#for AND operator
#If both are true then and then only true
val1 = True
val2 = False 
print("AND operator : ", val1 and val2)
val3 = True
val4 = True
print("AND operator : ", val3 and val4)

#for OR operator
#If any one of thse true then true
val1 = True
val2 = False
val3 = False 
val4 = False 
print("OR operator : ", val1 or val2)
print("OR operator : ", val3 or val4)
