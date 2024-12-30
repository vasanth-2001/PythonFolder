#parent/base class
class Person:
    def __init__(self,idCard,name):
        self.idCard=idCard
        self.name=name
    def DisplayInfo(self):
        print(f'Name:{self.name} \n Id Card: {self.idCard}')


#child class
class Employee(Person):
    def __init__(self,idCard,name,salary):
        super().__init__(idCard,name)
        self.salary=salary

obj1=Person(123,'Vasanth Rajendran')
obj1.DisplayInfo()

obj2=Employee(124,"Nirmal Kumar",15000)
obj2.DisplayInfo()
print(obj2.salary)
