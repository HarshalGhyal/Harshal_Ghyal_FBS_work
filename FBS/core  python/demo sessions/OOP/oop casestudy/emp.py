from abc import ABC,abstractmethod

class Emp(ABC):  # class
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
    @abstractmethod
    def calculatesalary(self):
        pass
    def __str__(self):
        return f'Id={self.id}\t Name={self.name} \t salary={self.sal}'