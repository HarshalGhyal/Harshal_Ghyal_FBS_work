#### Q03. Create a class MedicalStudent inherited from Student with following:
# i. Data members :Specialization
# ii. MarksOfInternship
# b. Add the following methods :
# i. Parameterized constructor
# ii. Display
# iii. Accept
# iv. override Method CalculateRank
# v. Override __str__ Method



class Student:
    def __init__(self, S_Id, name, age, percentage):
        self.S_Id = S_Id
        self.name = name
        self.age = age
        self.percentage = percentage

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


class Medical_student(Student):
    def __init__(self, S_Id, name, age, percentage, specilization, Marks_of_internship):
        super().__init__(S_Id, name, age, percentage)
        self.specilization = specilization
        self.Marks_of_internship = Marks_of_internship

    def display(self):
        super().display()
        print(f'Specilization={self.specilization}\nMarks_of_internship={self.Marks_of_internship}')

    def Accept(self):
        super().Accept()
        self.specilization = input("Enter Specilization: ")
        self.Marks_of_internship = int(input("Enter internship Marks: "))

    def CalculateRank(self, *students):
        rank = 1

        for student in students:
            if (student.percentage + student.Marks_of_internship) > \
               (self.percentage + self.Marks_of_internship):
                rank += 1

        return rank

    def __str__(self):
        return super().__str__() + \
               f'\nSpecilization={self.specilization}\nMarks_of_internship={self.Marks_of_internship}'


