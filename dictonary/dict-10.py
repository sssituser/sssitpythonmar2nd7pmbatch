d = {1:"raj",2:"ravi",3:"kiran",4:"charan",5:"mohan",6:"ratan"}

x = {key:value for key,value in d.items() if value.__contains__('n')}
print(x)


y ={key:value for key,value in d.items() if value.__contains__('r')}

print(y)
