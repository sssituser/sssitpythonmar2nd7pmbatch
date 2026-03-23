list =['arun','kiran','rakesh','sai','loukya','heswant']
print([element for element in list if element.__contains__('a')])
print([element for element in list if element.__contains__('r')])

li =[element for element in list if element.__contains__('k')]

print(li)