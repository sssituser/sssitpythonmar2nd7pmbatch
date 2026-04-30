class Stack:
    def __init__(self):
        self.items = []
    def push(self,item):
        self.items.append(item)
    def pop(self):
        if len(self.items)==0:
            return ""
        else:
            return self.items.pop()
    def peek(self):
        if len(self.items)==0:
            return ""
        else:
            return self.items[-1]
    def showitems(self):
        res =""
        if len(self.items)==0:
            return ""
        else:
            for i in self.items[::-1]:
                res = res+str(i)+"  "
            return res

st = Stack()
while True:
    choice = int(input('1.Push  2.Pop  3.Peek  4.Show Items\nEnter Your choice : '))
    match choice:
        case 1:
            item = int(input('Enter a number : '))
            st.push(item)
            if st.showitems()=="":
                print("Stack Is Empty")
            else:
                print(st.showitems())
        case 2:
            if st.showitems()=="":
                print("Stack is Empty") 
            else:
                print(f'Delete element is : {st.pop()}')
                print(st.showitems())
        case 3:    
            if st.peek()=="":
                print("Stack is Empty")
            else:
                print(f'Top or Peek Element in the stack is : {st.peek()}')
        case 4:
            if st.showitems()=="":
                print("Stack is Empty")
            else:
                print(st.showitems())
        
        
                       
        
    
    
        