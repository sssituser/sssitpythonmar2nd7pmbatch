num1 = int(input('Enter num1 : '))
num2 = int(input('Enter num2 : '))
choice = int(input('1.ADD\n2.SUB\n3.MUL\n4.DIV\n5.Remainder\nEnter ur choice : '))
match choice:
    case 1:
        print(f'Sum of {num1} + {num2} : {num1+num2}')
    case 2:
        print(f'Sub of {num1} - {num2} : {num1-num2}')
    case 3:
        print(f'Mul of {num1} * {num2} : {num1*num2}')
    case 4:
        print(f'Quo of {num1} // {num2} : {num1//num2}')
    case 5:
        print(f'Rem of {num1} % {num2} : {num1%num2}')
    case _:
        print("Invalid choice .... Plz select New and Right Choice ")       
print('Opertaion completed') 
        
    
        
        
        
        