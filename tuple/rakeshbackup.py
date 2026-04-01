t = (45,67,89,89,'abc',7+9j,[67,89],(67,89,90),4.5,True) 
print(t)
print(f"Elements present in the tuple is :{len(t)}")
t = (8,67,33,45,67,88,92)
print(max(t))
print(min(t))
print(sum(t))
print(sorted(t))
print(sorted(t,reverse=True))
#indexing
print(t[0])
print(t[-1])
#slicing
print(t[0:5])
print(t[:-4:-1])
#tuple comprehension
evens =[x for x in t if x%2==0]
odds = [x for x in t if x%2!=0]
sqrs =[x*x for x in t]
print(evens)
print(odds)
print(sqrs)
a = 10
b = 30
c = 40
x = a,b,c # packing
print('x = ',x,'Type of x ix ',type(x))
#unpacking
l,m,n = x
print(l)
print(m)

print(x*3)

print(x.index(10))