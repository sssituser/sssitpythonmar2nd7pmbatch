while True:
   try:
       num1 = int(input('Enter number1 : '))
       num2 = int(input('Enter number2 : '))
       print(f'quo ; {num1//num2}')
   except ValueError:
       print(f'Enter Only Integes(nums with out decimals')
   except ZeroDivisionError:
       print(f"num2 can't be zero")
   except Exception as e :
       print(e)     
   finally :
       print('Thanku visit again...')  
   
       
       