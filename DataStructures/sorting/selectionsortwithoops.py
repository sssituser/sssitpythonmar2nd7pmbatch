
class SelectionSort:
    def sort(self,li):
        for i in range(len(li)):
            for j in range(i+1,len(li)):
                if li[i]>li[j]:
                    li[i],li[j] = li[j],li[i]
s = SelectionSort()
li = [5,8,1,4,7]
print("Before sort=>")
print(li)
s.sort(li)
print("After sort=>")
print(li)
