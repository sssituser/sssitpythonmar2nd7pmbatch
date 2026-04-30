import os
class LinearSearchExample:
    def __init__(self):
        self.items = [23,45,67,89,90,12,33,44,55,66,77,88]
    
    def add(self,item):
        self.items.append(item)
        os.system('cls')
    
    def search(self,item):
        index = -1
        for i in range(len(self.items)):
            if item == self.items[i]:
                index = i   
        os.system('cls')  
        if index == -1:
            return f"{item} not Found"
        else:
            return f"{item} found at {index} location"
        
        
        
        
        
ls = LinearSearchExample()
while True:
    choice = int(input('1.Add\n2.Search\nEnter Your choice : '))
    match choice:
        case 1:
            item = int(input('Enter a number : '))
            ls.add(item)
        case 2:
            item = int(input('Enter a number Search : '))
            print(ls.search(item))
        case _:
            os.system('cls')
            print("Invalid Choice")
                