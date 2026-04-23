queue = []
def getelements():
    for i in range(0,len(queue)):
        print(queue[i],end="  ")
while True:
    ch =int(input("\n1.Insert 2.Delete 3.Peek  4.Show Enter choice :"))
    match ch:
        case 1:
            val = int(input('Enter a number : '))
            queue.append(val)
            print(f'{val} is Added Succesfully to the queue')
            getelements()
        case 2:
            if len(queue)==0:
                print(f'Queue Is Empty, We cant delete')
            else:
                print(f'Deleted element is : {queue[0]}')
                queue.remove(queue[0])
                getelements()
        case 3:
             if len(queue)==0:
                print(f'Queue Is Empty, No peek element')
             else:
                 print(f'Peek element :{queue[0]}')
        case 4:
            if len(queue)==0:
                print('No Elements to display')
            else:
                getelements()
        case _:
            print(f'Invalid choice....')                    
            
                