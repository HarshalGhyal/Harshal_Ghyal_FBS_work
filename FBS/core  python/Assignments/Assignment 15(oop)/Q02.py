#### Q2. Create a class Product with members as pid,pname,price and quantity .Add following methods:
# d. Constructor (Support both parameterized and parameterless)
# e. Destructor
# f. ShowBook

class Product:

    # Constructor - supports parameterless and parameterized
    def __init__(self, pid=0, pname="Unknown", price=0, quantity=0):
        self.pid = pid
        self.pname = pname
        self.price = price
        self.quantity = quantity

    # Destructor
    def __del__(self):
        print("Product object destroyed")

    # Display product details
    def ShowBook(self):
        print("Product ID :", self.pid)
        print("Product Name :", self.pname)
        print("Price :", self.price)
        print("Quantity :", self.quantity)


# Parameterless constructor
p1 = Product()
p1.ShowBook()



# Parameterized constructor
p2 = Product(101, "Laptop", 55000, 2)
p2.ShowBook()