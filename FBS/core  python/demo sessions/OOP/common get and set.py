class Emp:
    def __init__(self, id, name, sal):
        self.id = id
        self.name = name
        self.sal = sal

    def display(self):
        print(f'id={self.id}, name={self.name}, salary={self.sal}')

    # Common getter
    def get(self, attribute):
        return getattr(self, attribute)

    # Common setter
    def set(self, attribute, value):
        setattr(self, attribute, value)


e1 = Emp(111, 'harshal', 15000)
e2 = Emp(112, 'pratham', 15000)

e1.display()
e2.display()

# Getter
print(e1.get("id"))
print(e1.get("name"))
print(e1.get("sal"))

# Setter
e1.set("id", 101)
e1.set("name", "Rahul")
e1.set("sal", 25000)

e1.display()
e1.set("name","Virat")