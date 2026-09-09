from emp import Emp

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