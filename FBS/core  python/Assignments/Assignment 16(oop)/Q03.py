#### Q3. Create a class Shirt with members as sid,sname,type(formal etc), price and
# size(small,large etc) .Add following methods:
# j. Constructor (Support both parameterized and parameterless)
# k. Destructor
# l. ShowBook
# m. For each size of shirt price should change by 10%.
# (eg. If 1000 is price then small price = 1000, medium = 1100,large=1200 and
# xlarge=1300) Use static concept.

class Shirt:

    # Static variables
    small = 0
    medium = 10
    large = 20
    xlarge = 30

    # Constructor
    def __init__(self, sid=0, sname="Unknown", type="Unknown",
                 price=0, size="small"):
        self.sid = sid
        self.sname = sname
        self.type = type
        self.price = price
        self.size = size

    # Destructor
    def __del__(self):
        print("Shirt object destroyed")

    # Display shirt details
    def ShowBook(self):
        print("Shirt ID :", self.sid)
        print("Shirt Name :", self.sname)
        print("Type :", self.type)
        print("Price :", self.getPrice())
        print("Size :", self.size)

    # Calculate price according to size
    def getPrice(self):

        if self.size.lower() == "small":
            percentage = Shirt.small

        elif self.size.lower() == "medium":
            percentage = Shirt.medium

        elif self.size.lower() == "large":
            percentage = Shirt.large

        elif self.size.lower() == "xlarge":
            percentage = Shirt.xlarge

        else:
            percentage = 0

        final_price = self.price + (self.price * percentage / 100)

        return final_price


# Parameterless constructor
s1 = Shirt()
s1.ShowBook()


# Parameterized constructor
s2 = Shirt(101, "Oxford Shirt", "Formal", 1000, "Large")
s2.ShowBook()



s3 = Shirt(102, "Polo Shirt", "Casual", 1000, "Medium")
s3.ShowBook()


s4 = Shirt(103, "Party Shirt", "Casual", 1000, "XLarge")
s4.ShowBook()

