#### Q1. Write a Python program to find elements in a given set that are not in another set.

s={1,2,3,4,5}
s1={3,4,5,6}
def not_in_another_set(s,s1):
    li=[]
    for i in s:
        if i not in s1:
            li+=[i]
    return set(li)     

res=not_in_another_set(s,s1)
print(res)