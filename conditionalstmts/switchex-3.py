num1 = int(input('Enter num1 : '))
num2 = int(input('Enter num2 : '))
choice =input('+ => ADD\n- => SUB\n* => MUL\n// => DIV\n% => REM\nEnter Your choice :  ')

match choice:
    case '+':
        print(f'sum is {num1+num2}')
    case '-':
        print(f'sub is {num1-num2}')
    case '*':
        print(f'mul is {num1*num2}')
    case '//':
        print(f'quo is {num1//num2}')
    case '%':
        print(f'rem is {num1%num2}')

