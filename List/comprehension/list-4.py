li = [10,7,5,6,8,12,23,15]
print(li)
evenlist = [x for x in li if x%2==0]
print(evenlist)
oddlist =  [x for x in li if x%2!=0]

print(oddlist)

print([x for x in li if x%3==0 or x%5==0])
