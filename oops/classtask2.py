class listorder:
    def __init__(self):
        self.list1=[]
        self.totallist=0
        self.sum=sum
        self.maximum=None
        self.minimum=None
        
    def functioninput(self):
        self.totallist=int(input("total no of list : "))
        for i in range(self.totallist):
            self.addlist=int(input())
            self.list1.append(self.addlist)
            
        self.maximum=self.list1[0]
        self.minimum=self.list1[0]
        self.sum=0
        for n in self.list1:
            if n>self.maximum:
              self.maximum=n
            if n< self.minimum:
              self.minimum=n
            self.sum=self.sum+n 
        
        print(self.list1)
        print("maximum : ",self.maximum)
        print("Minimum :",self.minimum)
        print("Total : ",self.sum)

obj=listorder()
obj.functioninput()   