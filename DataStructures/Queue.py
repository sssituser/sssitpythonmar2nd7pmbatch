queue = []
while True:
    choice = int(input('1.Enque\n2.Dequeue\n3.Peek Element\n4.Show Elements\nEnter Your choice : '))
    match choice:
        case 1:
            num = int(input('Enter a number : '))
            queue.append(num)
        case 2 :
            print(f'Deleted Elemnet is {queue[0]}')
            queue.remove(queue[0])
        case 3:
            print(f'Peek Element in the Queue : {queue[0]}')
        case 4:
            if len(queue)==0:
                print("-----------------------------------------")
                print("Queue is Empty, You can add elements")
                print("-----------------------------------------")
            else:
                print("-----------------------------------------")
                for i in range(0,len(queue)):
                    print(queue[i])
                print("-----------------------------------------")
        case _:
            print("-----------------------------------------")
            print("Invalid Choice......Enter Proper Choice")
            print("-----------------------------------------")