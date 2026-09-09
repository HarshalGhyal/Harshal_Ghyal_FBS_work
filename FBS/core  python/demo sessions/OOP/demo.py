class Student:
    def __init__(self, rollno, name):
        self.__rollno = rollno
        self.__name = name

    def getRollNo(self):
        return self.__rollno

    def setRollNo(self, rno):
        self.__rollno = rno

    def __str__(self):
        return f"RollNo={self.__rollno} \tName={self.__name}"

    def __del__(self):
        print("Ghari ja OOP samapli")


class MedStudent(Student):
    def __init__(self, rollno, name, marks):
        super().__init__(rollno, name)
        self.__marks = marks

    def __str__(self):
        return super().__str__() + f"\t Mraks={self.__marks}"


s = Student(12, "Rahul")
m = MedStudent(12, "Swaraj", 444)
# print(s.__rollno)
# print(m.__name)
print(m.getRollNo())
m.setRollNo(1)
print(m)