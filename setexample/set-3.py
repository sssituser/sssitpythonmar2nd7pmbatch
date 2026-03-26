set1 = {10,40,50,30,20}
set2 = {1,4,5,6,7,10,20}

set3 = set1.union(set2)#set3 = set1|set2 
print(set1)
print(set2)
print(set3)
set4 = set1&set2
print(set4)

set5= set1.difference(set2)
print(set5)

set6 = set1.symmetric_difference(set2)
print(set6)
