class InvalideAgeExcption(Exception):
    def __init__(self,message):
        super().__init__(message)
        print('Invalid Age ....')
        
        
while True:
    try:
        age = int(input('Enter age : '))
        if age<0 or age>=150:
            raise InvalideAgeExcption("hi Im from try block....")
        else:
            print(f'You have entered valid Age')
    except Exception as e:
        print(e)