### Q10. Write a program to print list after removing even numbers ?

def rem_even(li):
    li1= []
     
    for i in li:
        if i % 2 !=0:
            li1.append(i)
            
    return li1

li=[1,2,3,4,5,6,7,8,9]

res=rem_even(li)

print(res)