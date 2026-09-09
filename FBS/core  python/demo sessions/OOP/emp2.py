# All oop concept in it:
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
class Hr(Emp):
    def __init__(self, id, name, sal,comm):
        super().__init__(id, name, sal)
        self.comm=comm

    def getcommision(self):
         return self.comm
    def setcommision(self,newcommision):
        self.comm = newcommision
    def calculatesalary(self):
         return self.sal+self.comm 
    def __str__(self):
        return super().__str__() + f'\t commision={self.comm}'
class Dev(Emp):
     def __init__(self, id, name, sal,bonus):
          super().__init__(id, name, sal)   
          self.bonus=bonus
     def getbonus(self):
          return self.bonus
     def setbonus(self,newbon):
          self.bonus=newbon
     def calculatesalary(self):
          return self.sal +self.bonus
     def __str__(self):
          return super().__str__()  + f'\t Bonus={self.bonus}'   
# e1=Emp(11,'harshal',12000) 
h1=Hr(12,'harry',13000,2500)    
d1=Dev(13,'pratham',15000,3500)
# print(e1)
print(h1)
print(d1)
print(d1.calculatesalary())