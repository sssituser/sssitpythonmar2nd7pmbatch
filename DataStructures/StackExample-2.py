stack = []
while True:
    choice = int(input("1.Insert\n2.Delete\n3.Top (Peek) Element\n4.Show All\nEnter ur choice : "))
    match choice:
        case 1:
            num = int(input('Enter a number : '))
            stack.append(num)
     
        case 2:
            print(f'Delete Element is {stack.pop()}')
        
        case 3:
            print(f'Top (Peek Element)of the Stack  : {stack[-1]}')
        case 4:
            if len(stack)==0:
                print('Stack is Empty..........')
            else:
                print("===============")
                for i in range(-1,-(len(stack)+1),-1):
                    print(stack[i])
        case _:
            print("Invalid choice....")