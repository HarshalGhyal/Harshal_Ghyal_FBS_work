#### Q8. Write a program to create a duplicate of an existing list. It should not point to same list.

def dupli_list(li):
    new=[]
    for i in li:
        new+=[i]
    return new

li=[1,2,3,4,5,6]    
li2=dupli_list(li)
print(li2)