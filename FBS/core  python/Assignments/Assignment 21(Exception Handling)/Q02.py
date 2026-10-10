#### Q.2. Create class television that has members to hold the model number ,screen size
# and price. Take a member function to take input from user, If more than 4 digits
# are entered for model number, if screen size is smaller than 12 inches or greater
# than 70 inches or if the price is negative or greater than 5000 Rs, then throw an
# exception.
# Write a main() that instantiates an object and allows the user to enter and display
# data. If exception is caught, replace all data member values with zero

class Television:
    def __init__(self):
        self.model_number = 0
        self.screen_size = 0
        self.price = 0

    def take_input(self):
        try:
            model = input("Enter model number : ").strip()
            size = float(input("Enter screen size (in inches): "))
            price = float(input("Enter price (in Rs.): "))

            # --- Validate model number ---
            if not model.isdigit() or len(model) > 4:
                raise ValueError("Model number must be a number with at most 4 digits.")

            # --- Validate screen size ---
            if size < 12 or size > 70:
                raise ValueError("Screen size must be between 12 and 70 inches.")

            # --- Validate price ---
            if price < 0 or price > 5000:
                raise ValueError("Price must be between 0 and 5000 Rs.")

            # --- All valid: assign ---
            self.model_number = int(model)
            self.screen_size = size
            self.price = price

        except ValueError as e:
            print(f"\nError: {e}")
            print("Resetting all values to zero.\n")
            self.model_number = 0
            self.screen_size = 0
            self.price = 0

    def display(self):
        print("----- Television Details -----")
        print(f"Model Number : {self.model_number}")
        print(f"Screen Size  : {self.screen_size} inches")
        print(f"Price        : Rs. {self.price}")


def main():
    tv = Television()
    tv.take_input()
    tv.display()


if __name__ == "__main__":
    main()