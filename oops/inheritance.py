# parent class
class person:
    def __init__(self,name,id):
        self.name=name
        self.id=id
    def displayinfo(self):
        print(f"Name : {self.name} \nId : {self.id}")
    
# child class  
class Employee(person):
    def __init__(self,name,id,salary):
        super().__init__(name,id)
        self.salary=salary
    def displayinfo(self):
        print(f"Name:{self.name} Id:{self.id} Salary:{self.salary}")
        
obj1=person("log",12)     
obj1.displayinfo()  
obj2=Employee("loki",123,2000)
obj2.displayinfo()