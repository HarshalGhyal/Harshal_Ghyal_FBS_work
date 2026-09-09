class Vehicle:
    def __init__(self,brand,model,type):
        self.brand=brand
        self.model=model
        self.type=type
    def dislpay(self):
        print(f'brand={self.brand}  model={self.model}  type={self.type}')   
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
    


v1=Vehicle('tata','nexon','car')   
v2=Vehicle('bajaj','pulsar','bike')   
v3=Vehicle('olectra','electro','bus')
v1.dislpay()
v2.dislpay() 
v3.dislpay()     
  