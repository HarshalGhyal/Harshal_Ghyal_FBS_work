#### Q2. Create a class Product with members as pid,pname,price and quantity .Add
# following methods:
# e. Constructor (Support both parameterized and parameterless)
# f. Destructor
# g. ShowBook
# h. Add static member discount.
# i. Provide methods for applying discount on price of product.


class Product:

    # Static member
    discount = 10       # 10% discount

    # Constructor
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

    # Apply discount
    def ApplyDiscount(self):
        discount_amount = self.price * Product.discount / 100
        self.price = self.price - discount_amount


# Parameterless constructor
p1 = Product()
p1.ShowBook()



# Parameterized constructor
p2 = Product(101, "Laptop", 50000, 2)

print("Before Discount:")
p2.ShowBook()

# Apply discount
p2.ApplyDiscount()

print("\nAfter Discount:")
p2.ShowBook()

