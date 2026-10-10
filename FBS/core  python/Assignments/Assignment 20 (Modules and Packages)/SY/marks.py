class SYMARKS:
    def __init__(self, computer_total, maths_total, electronics_total):
        # Initializing the subject totals
        self.computer_total = computer_total
        self.maths_total = maths_total
        self.electronics_total = electronics_total

    def display_marks(self):
        print("--- Second Year Marks ---")
        print(f"Computer Total: {self.computer_total}")
        print(f"Maths Total: {self.maths_total}")
        print(f"Electronics Total: {self.electronics_total}")



