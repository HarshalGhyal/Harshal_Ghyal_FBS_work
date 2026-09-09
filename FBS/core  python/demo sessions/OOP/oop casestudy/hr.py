from emp import Emp
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