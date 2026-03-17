num1 = int(input('Enter num1 : '))
num2 = int(input('Enter num2 : '))
choice = input('ADD\nSUB\nMUL\nDIV\nREM\nEnter ur choice : ')
match choice:
    case "ADD" | "add" | "Add":
        print(f'Sum of {num1} + {num2} : {num1+num2}')
    case "SUB" | "sub" | "Sub":
        print(f'Sub of {num1} - {num2} : {num1-num2}')
    case"MUL" | "mul"|"Mul":
        print(f'Mul of {num1} * {num2} : {num1*num2}')
    case "DIV" | "div"|"Div":
        print(f'Quo of {num1} // {num2} : {num1//num2}')
    case "REM"|"rem"|"Rem":
        print(f'Rem of {num1} % {num2} : {num1%num2}')
    case _:
        print("Invalid choice .... Plz select New and Right Choice ")       
print('Opertaion completed') 