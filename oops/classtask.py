class task:
    pi=3.14
    def __init__(self):
        self.radius=0
    def AcceptMethod(self):
        self.radius=int(input("Enter the Radius : "))
    def Area_of_the_circle(self):
        solution=self.pi*self.radius**2
        print("Answer :",solution)
obj1=task()
obj1.AcceptMethod()
obj1.Area_of_the_circle()
        
        
        