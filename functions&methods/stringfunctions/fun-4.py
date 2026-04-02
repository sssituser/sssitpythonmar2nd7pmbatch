s = 'kirankumar'
print(s) # kirankumar
x = s.upper()
print(x)
print(s) #

print(s.__contains__('ran'))
print(s.__contains__('run'))

print(s.count('a'))
print(s.capitalize())
print(s.__getitem__(0))
print(s.index('a'))

dob = "19-oct-1983"
print(dob.split('-'))
print(s.isalpha())
x ="19"
print(x.isnumeric(),x.isalpha())