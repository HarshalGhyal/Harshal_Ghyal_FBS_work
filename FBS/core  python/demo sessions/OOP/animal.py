class Animal:  
    def __init__(self, name, type):  
        self.name = name
        self.type = type

    def display(self):  
        print(f'name={self.name}, type={self.type}')
    def getname(self):
        return self.name
    def setname(self,newname):
        self.name=newname
    def gettype(self):
        return self.type
    def settype(self,newtype):
        self.type=newtype

a1 = Animal('Tiger', 'Wild')
a2 = Animal('Dog', 'Domestic')

a1.display()    
a2.display()  
a2.setname('lion')  
a2.display()