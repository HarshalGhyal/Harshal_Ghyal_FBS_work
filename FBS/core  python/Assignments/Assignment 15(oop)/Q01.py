#### Q1. Create a class Book with members as bid,bname,price and author.Add following methods:
# a. Constructor (Support both parameterized and parameterless)
# b. Destructor
# c. ShowBook



class Book:

    # Constructor
    def __init__(self, bid=0, bname="Unknown", price=0, author="Unknown"):
        self.bid = bid
        self.bname = bname
        self.price = price
        self.author = author

    # Destructor
    def __del__(self):
        print("Book object destroyed")

    # Display book details
    def ShowBook(self):
        print("Book ID :", self.bid)
        print("Book Name :", self.bname)
        print("Price :", self.price)
        print("Author :", self.author)


# Parameterless constructor
b1 = Book()
b1.ShowBook()



# Parameterized constructor
b2 = Book(101, "Python Programming", 500, "Ranjeet Kamble")
b2.ShowBook()