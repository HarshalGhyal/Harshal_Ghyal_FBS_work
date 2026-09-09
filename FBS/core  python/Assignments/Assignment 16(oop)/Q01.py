####Q1. Create a class Book with members as bid,bname,price and author.Add following
# methods:
# a. Constructor (Support both parameterized and parameterless)
# b. Destructor
# c. ShowBook
# d. Add static variable count and also maintain count of objects created.


class Book:

    # Static variable
    count = 0

    # Constructor
    def __init__(self, bid=0, bname="Unknown", price=0, author="Unknown"):
        self.bid = bid
        self.bname = bname
        self.price = price
        self.author = author

        # Increase object count
        Book.count += 1

    # Destructor
    def __del__(self):
        print("Book object destroyed")

    # Display book details
    def ShowBook(self):
        print("Book ID :", self.bid)
        print("Book Name :", self.bname)
        print("Price :", self.price)
        print("Author :", self.author)


# Parameterless object
b1 = Book()
b1.ShowBook()



# Parameterized objects
b2 = Book(101, "Python Programming", 500, "Ranjeet Kamble")
b2.ShowBook()

b3 = Book(102, "Java Programming", 600, "James Gosling")
b3.ShowBook()

# Display number of objects created
print("\nTotal objects created :", Book.count)

