#### Q10. Write a program to remove all occurrences of a given element in the list.

def remove_ele(li):
    ele=int(input("Enter element to remove:"))
    lit=[]
    if ele in li:
        for i in li:
            if i!=ele:
                lit+=[i]
        li=lit
        print(li)      
    else:
        print("element is not in the given list!")

li=[10,20,40,40,20,40,30,50,70,90]
remove_ele(li)
