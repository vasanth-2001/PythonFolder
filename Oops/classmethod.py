#class method
# class Student:
#     graduate='Hdfc Bank' #class variable
#     ROI=5
#     def graduate_in(cls):
#         print(cls.graduate)
# Student.graduate=classmethod(Student.graduate_in)  # convert using inbuilt method
# Student.graduate()
#class method
class Student:
    graduate='Hdfc Bank' #class variable
    ROI=5
    @classmethod        # convert by usiong decorative
    def graduate_in(cls):
        print(cls.graduate)
Student.graduate_in()

#static method
class Student:
    @staticmethod      
    def Rollnumber(y):
        print('Roll number',y)
Student.Rollnumber(101)
