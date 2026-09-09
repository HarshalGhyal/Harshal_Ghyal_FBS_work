class Emp:  # class
    def __init__(self,id,name,sal): # constructor method _init_
            self.id=id
            self.name=name
            self.sal=sal
    def display(self): # display method
          print(f'id={self.id}, name={self.name},salary={self.sal}')   
    def getid(self):
        return self.id
    def setid(self,newid):
        self.id=newid
    def getname(self):
        return self.name
    def setname(self,newname):
        self.name=newname    
    def getsalary(self):
        return self.sal
    def setsalary(self,newsalary):
        self.sal=newsalary    
        

e1=Emp(111,'harshal',15000) 
e2=Emp(112,'pratham',15000)
e1.display()    #object
e2.display()    #object  

      