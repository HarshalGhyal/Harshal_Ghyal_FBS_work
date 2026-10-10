from SY.marks import SYMARKS
from TY.ty_marks import TYMARKS
from student import Student

if __name__ == '__main__':
    sy = SYMARKS(computer_total=25, maths_total=90, electronics_total=88)
    ty = TYMARKS(theory=25, practical=25)

    student = Student(roll_number=101, name="Aditi Sharma",
                      sy_marks=sy, ty_marks=ty)

    student.display_result()