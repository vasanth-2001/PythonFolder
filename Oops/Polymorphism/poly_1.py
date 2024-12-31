#Example : Polymorphism and Inheritance (overriding)
class Transport:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model

    def Display(self):
        print(f'{self.brand} and {self.model}')
    
class Car(Transport):


class Bike(Transport):

class Boat(Transport):