class Person:
    def __init__(self,name,age,desgn):
        self.name=name
        self.age=age
        self.desgn=desgn

    def display(self):
        print(f'name:{self.name}  age:{self.age} desgn:{self.desgn}')    

    def getname(self):
        return self.name
    def setname(self,newname):
        self.name=newname
        
    def getage(self):
        return self.age
    def setage(self,newage):
        self.age=newage
    def getndesignation(self):
        return self.desgn
    def setname(self,newdesgn):
        self.desgn=newdesgn


p1=Person('harshal',21,'student')
p2=Person('Rahul',36,'psi')        

p1.display()
p2.display()
p2.setage(12)
print(p2.getage())
    