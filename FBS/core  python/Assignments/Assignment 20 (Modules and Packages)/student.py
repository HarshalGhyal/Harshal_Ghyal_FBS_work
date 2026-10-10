class Student:
    def __init__(self, roll_number, name, sy_marks, ty_marks):
        self.roll_number = roll_number
        self.name = name
        self.sy_marks = sy_marks       # an SYMARKS object
        self.ty_marks = ty_marks       # a TYMARKS object

    def computer_total(self):
        """Add SY Computer Total + TY Theory + TY Practical."""
        return (
            self.sy_marks.computer_total
            + self.ty_marks.theory
            + self.ty_marks.practical
        )

    def grade(self):
        """Return grade based on total Computer marks."""
        total = self.computer_total()
        if total >= 70:
            return "A"
        elif total >= 60:
            return "B"
        elif total >= 50:
            return "C"
        elif total >= 40:
            return "Pass Class"
        else:
            return "Fail"

    def display_result(self):
        print("=" * 40)
        print(f" Roll Number : {self.roll_number}")
        print(f" Name        : {self.name}")
        print("-" * 40)
        print(f" SY Computer : {self.sy_marks.computer_total}")
        print(f" TY Theory   : {self.ty_marks.theory}")
        print(f" TY Practical: {self.ty_marks.practical}")
        print("-" * 40)
        print(f" Computer Total : {self.computer_total()}")
        print(f" Grade          : {self.grade()}")
        print("=" * 40)