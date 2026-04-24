class StackExample:
    def __init__(self): # constructor
        self.items = []
    def push(self,item):
        self.items.append(item)
    def pop(self):
        if len(self.items)==0:
            return "Stack is Empty"
        else:
            return f"Deleted element is {self.items.pop()}"
    def peek(self):
        if len(self.items)==0:
            return "Stack is Empty"
        else:
            return f"Top(Peek) Element in the Stack is : {self.items[-1]}"
    def showitems(self):
        if len(self.items)==0:
            return "Stack is Empty"
        else:
           res = ''
           for i in range(len(stack.items)-1,-1,-1): #
               res = res+str(stack.items[i])+" "
        return res
        
stack =StackExample()
while True:
    ch = int(input('1.Inesrt   2.Delete    3.Top    4.Show Elements : Enter ur choice : '))
    match ch:
        case 1:
            num = int(input('Enter number : '))
            stack.push(num)
            print(stack.showitems())
        case 2:
            print(stack.pop())
            print(stack.showitems())
        case 3:
            print(stack.peek())
        case 4:
            print(stack.showitems())
        case _:
            print("Invalid choice........")
            
                    

    