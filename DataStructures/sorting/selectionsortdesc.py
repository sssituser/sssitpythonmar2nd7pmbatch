list=[12,23,45,56,34]
print("Displaying the element Befor sorting")
print(list)
for i in range(len(list)):
    for j in range(i+1,len(list)):
        if list[i]<list[j]:
            temp = list[i]
            list[i] = list[j]
            list[j] = temp
print("Elements after sorting")
print(list)
                        #Session starts soon
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        