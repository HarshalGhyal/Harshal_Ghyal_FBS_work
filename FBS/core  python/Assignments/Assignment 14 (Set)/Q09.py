#### Q9. Write a Python program to find all the unique combinations of 3
# numbers from a given list of numbers, adding up to a target number.

li=[0,1,2,3,4,5,6,7,8,9,10]
t=5
def three_sum_element_fortarget(li,t):
    li1=[]
    for i in li:
        for j in li:
            for k in li:
                if i+j+k==t:
                    li1.append(tuple(sorted((i,j,k))))
    li1=set(li1)
    print(li1)
three_sum_element_fortarget(li,t)    