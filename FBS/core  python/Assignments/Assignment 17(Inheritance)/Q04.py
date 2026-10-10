# 4. Create a class College which has collection of students. Add the
# following methods :
# a. Parameteried constructor for number of students.
# b. AddStudent
# c. GetStudent
# d. RemoveStudent
# e. Override __str__ Method



class Student:

    def __init__(self, id, name, age, per):
        self.id = id
        self.name = name
        self.age = age
        self.per = per

    def getId(self):
        return self.id
    def setId(self, id):
        self.id = id

    def getname(self):
        return self.name
    def setname(self, name):
        self.name = name

    def getage(self):
        return self.age
    def setage(self, age):
        self.age = age

    def getper(self):
        return self.per
    def setper(self, per):
        self.per = per

   
    def calculateRank(self):

        if self.per >= 75:
            return "Distinction"
        elif self.per >= 60:
            return "First Class"
        elif self.per >= 50:
            return "Second Class"
        elif self.per >= 35:
            return "Pass"
        else:
            return "Fail"

    # __str__ method
    def __str__(self):
        return (
            f"Student Id: {self.id}\n"
            f"Name: {self.name}\n"
            f"Age: {self.age}\n"
            f"Percentage: {self.per}\n"
            f"Rank: {self.calculateRank()}"
        )


# ============================================================
# Engineering Student
# ============================================================

class EnggStudent(Student):

    def __init__(self, id, name, age, per, branch, IM):
        super().__init__(id, name, age, per)

        self.branch = branch
        self.im = IM

    def getbranch(self):
        return self.branch
    def setbranch(self, branch):
        self.branch = branch

    def getim(self):
        return self.im
    def setim(self, im):
        self.im = im

    def calculateRank(self):
        total = self.per + self.im

        if total >= 90:
            return "Distinction"
        elif total >= 75:
            return "First Class"
        elif total >= 60:
            return "Second Class"
        elif total >= 35:
            return "Pass"
        else:
            return "Fail"

    # Override __str__()
    def __str__(self):
        return (
            super().__str__()
            + f"\nBranch: {self.branch}"
            + f"\nInternal Marks: {self.im}"
        )


# ============================================================
# Medical Student
# ============================================================

class MedicalStudent(Student):

    def __init__(self, id, name, age, per, specialization, MoI):
        super().__init__(id, name, age, per)

        self.specialization = specialization
        self.moi = MoI

    def getSpecialization(self):
        return self.specialization
    def setSpecialization(self, sp):
        self.specialization = sp

    def getMoI(self):
        return self.moi
    def setMoI(self, moi):
        self.moi = moi

   
    def calculateRank(self):
        total = self.per + self.moi

        if total >= 90:
            return "Distinction"
        elif total >= 75:
            return "First Class"
        elif total >= 60:
            return "Second Class"
        elif total >= 35:
            return "Pass"
        else:
            return "Fail"

    # Override __str__()
    def __str__(self):
        return (
            super().__str__()
            + f"\nSpecialization: {self.specialization}"
            + f"\nInternship Marks: {self.moi}"
        )


# ============================================================
# College
# ============================================================

class College:

    def __init__(self, noStudent):
        self.noStudent = noStudent
        self.students = []

    # Add Student
    def addStudent(self, student):

        if len(self.students) < self.noStudent:
            self.students.append(student)
            print("Student added successfully.")

        else:
            print("College is full.")

    # Get Student
    def getStudent(self, studentId):

        for student in self.students:

            if student.id == studentId:
                return student

        return None

    # Remove Student
    def removeStudent(self, studentId):

        for student in self.students:

            if student.id == studentId:
                self.students.remove(student)
                print("Student removed successfully.")
                return

        print("Student not found.")

    # __str__ method
    def __str__(self):

        result = f"College Capacity: {self.noStudent}\n"
        result += f"Total Students: {len(self.students)}\n\n"

        for student in self.students:
            result += str(student)
            result += "\n-------------------------\n"

        return result


# ============================================================
# MAIN PROGRAM
# ============================================================

# Engineering Students

engg1 = EnggStudent(
    101,
    "Purva",
    21,
    80,
    "Computer Science",
    10
)

engg2 = EnggStudent(
    102,
    "Rahul",
    22,
    70,
    "Mechanical",
    15
)


# Medical Student

medical1 = MedicalStudent(
    201,
    "Priya",
    23,
    85,
    "Cardiology",
    5
)


# Normal Student

student1 = Student(
    301,
    "Amit",
    20,
    65
)


# Creating College

college = College(5)


# Adding Students

college.addStudent(engg1)
college.addStudent(engg2)
college.addStudent(medical1)
college.addStudent(student1)


# Display all students

print("\n========== ALL STUDENTS ==========")
print(college)


# Get Student

print("\n========== GET STUDENT ==========")

student = college.getStudent(101)

if student:
    print(student)

else:
    print("Student not found.")


# Remove Student

print("\n========== REMOVE STUDENT ==========")

college.removeStudent(102)


# Display after removing

print("\n========== AFTER REMOVING ==========")
print(college)