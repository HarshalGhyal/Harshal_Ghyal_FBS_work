#### 2. Create a class Distance with data members as km,m and cm and add following methods :
# a. Constructor
# b. Destructor
# c. Overload +,- operator


class Distance:
    def __init__(self,km,m,cm):
        self.km=km
        self.m=m
        self.cm=cm
    def __del__(self):
        print('Object destroyed')
    def get_km(self):
        return self.km
    def set_km(self,new_km):
        self.km=new_km
    def get_m(self):
        return self.m 
    def set_m(self,new_m):
        self.m=new_m
    def get_cm(self):
        return self.cm
    def set_cm(self,new_cm):
        self.cm=new_cm
    def __add__(self, other):
        total_cm=self.cm+other.cm
        rem_m=total_cm//100
        total_cm=total_cm%100
        total_m=self.m+other.m+rem_m
        rem_km=total_m//1000
        total_m=total_m%1000
        total_km=self.km+other.km+rem_km
        return Distance(total_km,total_m,total_cm)   
    
    def __str__(self):
        return f'Km={self.km} \nM={self.m}\nCm={self.cm}'
d1=Distance(12,455,600)
d2=Distance(4,777,899)
d3=d1+d2
print(d3)    
           
         
       