#parent/base class
class Person:
    def __init__(self,idCard,name):
        self.idCard=idCard
        self.name=name
    def DisplayInfo(self):
        print(f'Name:{self.name} \n Id Card: {self.idCard}')


#child class
class Employee(Person):
    def show(self):
        print('Inside show')

obj1=Employee(123,'Vasanth Rajendran')
obj1.DisplayInfo()
obj1.show()
