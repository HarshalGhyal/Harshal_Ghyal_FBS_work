#### Q4. Write a Python program that finds all pairs of elements in a list whose
# sum is equal to a given value.

li=[1,2,3,4,5,6,7,8,9]
t=17
def sum_pairs(li,t):
    li1=[]
    for i in li:
        for j in li:
            if i+j==t :
                li1+=[tuple(sorted((i,j)))]     #for unique pairs
                # li1+=[(i,j)]
    return set(li1)

res=sum_pairs(li,t)
print(res)
    