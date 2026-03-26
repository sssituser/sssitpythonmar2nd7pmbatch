tu = (45,66,78,90,22,48,66,44,45,66,66)

print(tu[0:])
print(tu[0:5])
print(tu[0::3])
print(tu[::-1])

print(f'max  ={max(tu)}\t min = {min(tu)}\t No of elements in the tuple : {len(tu)}')
print(f'sum of the elments of the tuple : {sum(tu)}')

print(tu)
print(sorted(tu))
print(sorted(tu,reverse=True))
print(tu.count(66))
print(tu[0])
print(tu.index(66))