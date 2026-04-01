'''
write a program to find the frequency of the characters of a given name
arunkumar
a - 2
k - 1
m - 1
n - 1
r - 1
u - 2
'''
d = {}
name = 'arunkumar'
for x in name: #abac
    if d.__contains__(x):
        val = d.get(x)
        d[x] = val+1
    else:
        d[x] = 1
print(d)
    