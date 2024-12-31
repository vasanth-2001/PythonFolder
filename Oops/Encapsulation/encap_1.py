#Private : (__double underscore)

class Employee:
    def __init__(self,name,salary):
        self.name=name   #public
        self.__salary=salary
    
    def DisplaySalaryInfo(self):
        print(f'{self.name} holding salary of {self.__salary}')

e1 =Employee('Vasanth',25000)
print(e1.name)
# print(e1.__salary)   # private  #cannot access outside the class
print(e1._Employee__salary)  #Access
e1.DisplaySalaryInfo()
print(e1.__salary)