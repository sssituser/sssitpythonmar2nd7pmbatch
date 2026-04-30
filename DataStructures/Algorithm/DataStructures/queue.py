class Queue:
    def __init__(self):
        self.items = []
    def enque(self,item):
        self.items.append(item)
    def deque(self):  
            if len(self.items)!=0:
                val = self.items[0]
                self.items.remove(self.items[0])
                return f'Deleted element is : {val}'
            else:
                return
    def peek(self):
        if len(self.items)==0:
            return "Queue is Empty"
        else:
            return f'Peek or Top element in the Queue : {self.items[0]}'
    def showitems(self):
        res = ""
        if len(self.items)==0:
            res =  "Queue  is Empty"
        else:
            for item in self.items:
                res = res + str(item)+"  "
        return res
q = Queue()
while True:
    ch = int(input('\n1.Enque 2.Deque 3.Peek  4.ShowItems\nEnter your choice : '))
    match ch:
        case 1:
            item = int(input('Enter a number : '))
            q.enque(item)
            print(q.showitems())
        case 2:
            print(q.deque())
            if q.showitems()!="":
             print(q.showitems())
        case 3:                    
            print(q.peek())
        case 4:
            print(q.showitems())
        case _:
            print("Invalid choice...,Enter Propser choice [1,2,3,4]")
        