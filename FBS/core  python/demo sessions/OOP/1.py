# a=10
# b=20
# c=a+b
# print(c)

# a='harshal'
# b='ghyal'
# print(a+b)

# l1=[1,2,3,4]
# l2=[5,6,7,8]
# print(l1+l2)

class Time:
    def __init__(self,hr,min,sec):
        self.hr=hr
        self.min=min
        self.sec=sec
    def gethr(self):
        return self.hr
    def sethr(self,newhr):
        self.hr=newhr
    def getmin(self):
        return self.min  
    def setmin(self,newmin):
        self.min=newmin
    def getsec(self):
       return self.sec
    def setsec(self,newsec):
        self.sec=newsec
    def __add__(self, other):
        totalsec=self.sec+other.sec
        remmin=totalsec//60
        totalsec=totalsec%60
        totalmin=self.min+other.min+remmin
        remhr=totalmin//60
        totalmin=totalmin%60
        totalhr=self.hr+other.hr+remhr
        return Time(totalhr,totalmin,totalsec)

    def __str__(self):
        return f'\thour={self.hr}\t\tminute={self.min}\tsecond={self.sec}'    

t1=Time(2,45,50)  
t2=Time(3,20,30)  
print(t1+t2)



