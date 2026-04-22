stack = []
while True:
    choice = int(input('1.Insert\n2.Delete\n3.Top(Peek) Element\n4.Show All\nEnter you choice : '))
    match choice:
        case 1:
            element = int(input('Enter a number : '))
            stack.append(element)
            
        case 2:
            print(f'Deleted element is : {stack.pop()}')
            
        case 3:
            print(f'Top element in the Stack is : {stack[-1]}')
            
        case 4:
            if len(stack)==0:
                print("Stack Is Empty, You can Add element")
            else:
                print("=======")
                for i in range(-1,-(len(stack)+1),-1):
                    print(stack[i])
                print("=======")
        case _:
            print('Invalid choice,Enter choice from 1 to 4 ')