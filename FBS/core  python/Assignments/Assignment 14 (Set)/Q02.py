#### Q2. Write a Python program to remove the intersection of a second set with a first set.

s={1,2,3,4,5}
s1={5,6}
def not_in_another_set(s,s1):
    li=[]
    for i in s:
        if i  in s1:
            li+=[i]
    s=list(s)
    for j in li:
        s.remove(j)
    return set(s)    


res=not_in_another_set(s,s1)
print(res)