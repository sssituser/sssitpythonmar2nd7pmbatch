class BubbleSort:
    def sort(self,li):
        n = len(li)
        for i in range(n):
            for j in range(0,n-i-1):
                if li[j]>li[j+1]:
                    li[j],li[j+1]=li[j+1],li[j]
li = [5,8,1,4,7]
b = BubbleSort()
print("Before sorting ")
print(li)
b.sort(li)
print("After sorting########")
print(li)
                    