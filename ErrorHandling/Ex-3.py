while True:
    try:
        num1 = int(input('Enter num1 : '))
        num2 = int(input('Enter num2 : '))
     
        print(f'Sum is : {num1 + num2}')
           
        if num2 == 0:
            raise ZeroDivisionError("You cannot divide by zero.....")
        print(f'Quotient is : {num1 // num2}')
    
    except ValueError:
        print('Enter only integers')
    
    except ZeroDivisionError as e:
        print(f'num2 cannot be zero: {e}')
    except e:
        print(e)
    finally :
	    print('Thanku visit again')
    