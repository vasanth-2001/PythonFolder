class operation:
    def __init__(self):
        self.ListValue=[]
        self.largest=0
        self.smallest=0
        self.add=0
        self.n=0
    
    def Createlist(self):
        self.n=int(input("how many value add in list : "))
        # print(self.n)
        for i in range(self.n):
            self.ListValue.append(int(input()))
        print("Values in List : ",self.ListValue)
    def maximum(self):
        self.largest=self.ListValue[0]
        for i in range(len(self.ListValue)):
            if(self.ListValue[i]>self.largest):
                self.largest=self.ListValue[i]
        return self.largest
    def minimum(self):
        self.smallest=self.ListValue[0]
        for i in range(len(self.ListValue)):
            if(self.ListValue[i]<self.smallest):
                self.smallest=self.ListValue[i]
        return self.smallest
    
    def addition(self):
        for i in self.ListValue:
            self.add+=i
        return self.add


obj1=operation()
obj1.Createlist()
print("Maximum number in the list",obj1.maximum())
print("Minimum number in the list",obj1.minimum())
print("Adding the number in the list",obj1.addition())