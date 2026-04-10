class Student:
    def setstudent(self):
        self.stuid = int(input('Enter Student ID : '))
        self.stuname = input('Enter Name : ')
        self.stumarks = int(input('Enter Marks : '))
    def showstudent(self):
        print(f'Student ID : {self.stuid}')
        print(f'Student Name  : {self.stuname}')
        print(f'Student Marks : {self.stumarks}')
print("=================Student-1=====================")
s1 = Student()
s1.setstudent()
s1.showstudent()
print("=================Student-2=====================")
s2 = Student()
s2.setstudent()
s2.showstudent()

