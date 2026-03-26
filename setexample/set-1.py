st = {10,10,'abc',6.7,(9,8),6+9j}
print(st)
#print(st[0]) indexing is not possible in set
st.add(897)
st.add(True)
print(st)
print(f'Deleted element is : {st.pop()}')
print(st)
st.remove(10)
#st.remove(100) the elements which are not present in the set, if try to remove we get keyerror
print(st)
st.discard(True)
st.discard(10000)
print(st)
st.update(["kkkk",900,6.7])
print(st)