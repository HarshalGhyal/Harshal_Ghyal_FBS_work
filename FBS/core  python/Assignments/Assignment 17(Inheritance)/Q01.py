#### 1. Create a class Student with following
# a. data members :
# i. StudentId
# ii. Name
# iii. Age
# iv. Percentage
# b. Add the following methods :
# i. Parameterized constructor
# ii. Display
# iii. Accept
# iv. Method CalculateRank
# v. Override __str__ Method



class Student:
    def __init__(self,S_Id,name,age,percentage):
        self.S_Id=S_Id
        self.name=name
        self.age=age
        self.percentage=percentage
    def display(self):
        print(f'Student_Id={self.S_Id}\nStudent_name={self.name}\nStudent_age={self.age}\nPercentage={self.percentage}')    
    def Accept(self):
        self.S_Id = int(input("Enter Student ID: "))
        self.name = input("Enter Name: ")
        self.age = int(input("Enter Age: "))
        self.percentage = float(input("Enter Percentage: "))    
   
    def CalculateRank(self, *students):
        
        rank = 1

        for student in students:
            if student.percentage > self.percentage:
                rank += 1

        return rank
    def __str__(self):
        return f'Student_Id={self.S_Id}\nStudent_name={self.name}\nStudent_age={self.age}\nPercentage={self.percentage}'  

        
s1 = Student(101, "Rohit", 20, 87)
s2 = Student(102, "Amit", 21, 92)
s3 = Student(103, "Rahul", 20, 78)
s1.CalculateRank(s1,s2,s3)
s2.CalculateRank(s1,s2,s3)
print(s1)
