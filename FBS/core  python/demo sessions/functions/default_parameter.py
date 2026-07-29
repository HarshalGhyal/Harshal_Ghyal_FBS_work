#1. to make parameter optional
#2.assign value to parameter in fuction defination.
#3.if we pass value to default parameter it takes pass value 
# if we dont pass value to default parameter it takes default value.
#4.flow from right to left

def emp(id,name=None,sal=20000,dept='IT'):

    print("Id:",id)
    print('Name:',name)
    print('Salary:',sal)
    print('department:',dept)

emp(101,'om',50000,'da')  
print('#####################') 
emp(102,'jayant',60000)
print('#####################')
emp(103,'pratiksha')