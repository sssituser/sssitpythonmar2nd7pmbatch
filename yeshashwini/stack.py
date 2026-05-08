li = []
def getelements(li):
    for i in range(-1,-(len(li)+1),-1):
                print(li[i])
while True:
    choice = int(input("1.Insert\n2.Delete\n3.Peek or Top\n4.Show\nEnter your choice : "))
    match choice:
        case 1:
            key = int(input('Enter a number : '))
            li.append(key)
            getelements(li)
            
          
        case 2:
            if len(li)==0:
                print("Stack is Empty...")
            else:
                print(f'Deleted Eelement : {li.pop()}')
                getelements(li)
        case 3:
            if len(li)==0:
                print("Stack is Empty...")
            else:
              print(f'Top (Peek) Eelement : {li[-1]}')
        case 4:
            if len(li)==0:
                print("Stack is Empty...")
            else:
              getelements(li)
              
            
            
            