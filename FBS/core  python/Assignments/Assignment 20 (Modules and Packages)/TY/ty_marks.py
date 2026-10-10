class TYMARKS:
    def __init__(self, theory, practical):
        self.theory = theory
        self.practical = practical

    def display_marks(self):
        print("--- Third Year Marks ---")
        print(f"Theory: {self.theory}")
        print(f"Practical: {self.practical}")