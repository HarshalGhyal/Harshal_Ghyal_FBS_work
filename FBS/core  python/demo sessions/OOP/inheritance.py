class FbsStudent:
    stCount=0  #static keyword
    # NameofIn ="FBS"
    # def ImpInfo():  # static method
    #     print(f"I am from {FbsStudent.NameofIn}")

    def __init__(self,frn,name,batch):
        self.frn = frn
        self.name=name
        self.batch=batch
        FbsStudent.stCount+=1

    def getFrn(self):
        return self.frn
    def setFrn(self,newFrn):
        self.frn=newFrn

    def getName(self):
        return self.name
    def setName(self,newName):
        self.name=newName

    def getBatch(self):
        return self.batch
    def setBatch(self,newBatch):
        self.batch=newBatch

    def display(self):
        print(f"FRN no:{self.frn}, Name:{self.name}, Batch={self.batch}")

# s1=FbsStudent(53,"poorva","june26")
# s2=FbsStudent(54,"Prachi","june26")


class PlacedStudent(FbsStudent):
    def __init__(self, frn, name, batch,cName): #placedStudent
        super().__init__(frn, name, batch) #FbsStudent
        self.cName=cName

    def getFrn(self):
        return super().getFrn()
    def setFrn(self, newFrn):
        return super().setFrn(newFrn)

    def getName(self):
        return super().getName()
    def setName(self, newName):
        return super().setName(newName)

    def getBatch(self):
        return super().getBatch()
    def setBatch(self, newBatch):
        return super().setBatch(newBatch)

    def getcName(self):
        return self.cName
    def setcName(self,cName):
        self.cName=cName

    def display(self):
        super().display()
        print(f"cName={self.cName}")

s1=FbsStudent(53,"poorva","june26")
s2=FbsStudent(54,"Prachi","june26")
s3=PlacedStudent(55,"Ninad","june25","Infosys")
print(FbsStudent.stCount)
s3.display()
# FbsStudent.ImpInfo()