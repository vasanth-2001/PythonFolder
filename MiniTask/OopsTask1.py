class AreaOfCircle:
    pi=3.14
    def __init__(self):
        self.Radius=""
    def AcceptMethod(self,Radius):
        self.Radius=Radius
    def Areaofcircle(self):
        circle=self.pi*self.Radius**2
        print(circle)
obj1=AreaOfCircle()
obj1.AcceptMethod(int(input('Enter the radius')))
obj1.Areaofcircle()


