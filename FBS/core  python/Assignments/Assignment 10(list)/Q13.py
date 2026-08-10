#### Q13 . Write a program to print list after removing even numbers.

def rem_even(li):
    lit=[]
            
    for i in li:
        if i%2!=0:
            lit+=[i]
    li=lit
    print("list after removing even numbers:",li) 

li=[1,2,3,4,5,6,7,8,9,10]    
rem_even(li)