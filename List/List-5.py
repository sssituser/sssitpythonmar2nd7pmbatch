li = [10,40,60,80]

print(dir(li))

print("Total elements present in the list : ",li.__len__())
print(li)
print(f'Before Deleting the elmenets  from the list')
li.pop() # deleting the last element of the list

print(li)
li.append(19)
li.append(30)
li.append(60) # inserting the element at the end of the list
li.insert(6,100)  #Add element to list for the index.

print(li)
li.remove(10)
print(li)
