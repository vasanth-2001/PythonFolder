class operation:
    def __init__(self):
        self.ListValue=[]
        self.largest=0
        self.smallest=0
        self.add=0
        self.n=0
    
    def Createlist(self):
        self.n=int(input("how many value add in list"))
        print(self.n)
        for i in range(len(self.n)):
            self.ListValue.append(int(input()))
        
    def maximum(self):
        self.largest=self.ListValue[0]
        for i in range(len(self.ListValue)):
            if(self.ListValue[i]>self.largest):
                self.largest=self.ListValue[i]
        return self.largest
    def minimum(self):
        self.smallest=self.ListValue[0]
        for i in range(len(self.ListValue)):
            if(self.ListValue[i]>self.smallest):
                self.smallest=self.ListValue[i]
        return self.smallest


obj1=operation()
obj1.Createlist()
print(obj1.maximum())