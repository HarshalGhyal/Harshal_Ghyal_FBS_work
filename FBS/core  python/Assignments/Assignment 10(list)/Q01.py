#### Q1. Write a program to find sum of all elements of list.
def list_creation():
    n=int(input("enter number of elements:"))
    li=[]

    for i in range(0,n):
        num=int(input(f"Enter number at index {i}:"))
        li+=[num]
    return li

def sum_list(li,total=0):
    total=0
    for i in li:
        total+=i
    return total    


li=list_creation()  

sum=sum_list(li)
print("sum of all elements in given list is:",sum)