#### Q12. Write a program to create three lists of numbers, their squares and cubes

def list_creation():
    n=int(input("enter number of elements:"))
    li=[]
    square=[]
    cube=[]

    for i in range(0,n):
        num=int(input(f"Enter number at index {i}:"))
        li+=[num]
        square+=[num**2]
        cube+=[num**3]

    print("list of numbers:",li)   
    print("list of squares of numbers:",square)
    print("list of cube of numbers:",cube) 

list_creation()    
            
    
