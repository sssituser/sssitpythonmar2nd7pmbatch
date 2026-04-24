class QueueExample:
    def __init__(self):#constructor
        self.items = []
    def enque(self,item):
        self.items.append(item)
       
    def deque(self):
        if len(self.items) == 0:
            return "Queue is Empty"
        else:
            value = self.items[0]
            self.items.remove(value)
            return f'Deleted element is {value}'

    def peek(self):
        if len(self.items)==0:
            return "Queue is Empty"
        else:
            return f"Peek Element in the Queue : {self.items[0]}"
    def show(self):
        res = ""
        if len(self.items) == 0:
            res = "Queue is Empty"
        else:
            for i in range(0,len(self.items)):
                res+=str(self.items[i])+" "
        return res
q = QueueExample()
while True:
    ch = int(input("1.Enque   2.Deque   3.Peek    4.Show    Enter Your choice : "))
    match ch:
        case 1:
            item = int(input('Enter Element : '))
            q.enque(item)
            print(q.show())
        case 2:
            print(q.deque())
            print(q.show())
        case 3:
            print(q.peek())
        case 4:
            print(q.show()) 
        case _:
            print(f"Invalid choice:{ch} , Enter Proper choice 1,2,3,4")       