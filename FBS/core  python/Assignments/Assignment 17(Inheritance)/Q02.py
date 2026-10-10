#### Q2. Create a derived class from Student as EnggStudent with :
# a. Data members as :
# i. Branch
# ii. InternalMarks
# b. Add the following methods :
# i. Parameterized constructor
# ii. Display
# iii. Accept
# iv. override Method CalculateRank
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

class Engg_Student(Student):
    def __init__(self, S_Id, name, age, percentage,branch,internal_marks):
        super().__init__(S_Id, name, age, percentage)
        self.branch=branch
        self.internal_marks=internal_marks
    def display(self):
        super().display() 
        print(f'Branch={self.branch}\nInternalMarks={self.internal_marks}')

    def Accept(self):
        super().Accept()
        self.branch=input('Enter Branch:')
        self.internal_marks=int(input("Enter internal Marks:"))
    def CalculateRank(self, *students):
        rank = 1

        for student in students:
            if (student.percentage + student.internal_marks) > (self.percentage + self.internal_marks):
                rank += 1

        return rank
    def __str__(self):
        return super().__str__() + f'Branch={self.branch}\nInternalMarks={self.internal_marks}'
        

    