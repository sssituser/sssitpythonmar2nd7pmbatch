set1 = {40,11,32,67,21,50}
print(len(set1))
print(max(set1))
print(min(set1))
print(sum(set1))
print(sorted(set1))
print(sorted(set1,reverse=True))
evennums = {x for x in set1 if x%2==0}
print(evennums)
oddnums = {x for x in set1 if x%2 !=0}
print(oddnums)
