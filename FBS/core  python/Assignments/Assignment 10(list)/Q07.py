#### Q7. Write a program to create a new list from existing list which contains cube of
# each number of list.


def cube_list(li):
    new=[]
    for ele in li:
        new+=[ele**3]
    return new

li=[2,4,8,16,32]   
cube=cube_list(li) 
print(cube)