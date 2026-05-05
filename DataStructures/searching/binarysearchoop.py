class BinarySearch:
    def __init__(self):
        self.items =[10,20,30,40,45,50,52,67,88,99]
    def search(self,key):
        low = 0
        high = len(self.items)-1
        while low<=high:
            mid = (low+high)//2
            if self.items[mid]==key:
                return f'{key} found at {mid} location'
            elif key<self.items[mid]:
                high = mid-1
            else:
                low = mid+1
        return f'{key} not found'        
            
bs = BinarySearch()
key = int(input('Enter element to be searched : '))
print(bs.search(key))