#### Q4. Write a program to reverse the list.
# Method 1:
def rev_list(li):
    lii=[0]*len(li)
    ind=0
    for i in range(len(li)-1,-1,-1):
        lii[ind]=li[i]
        ind+=1
    li=lii
    print(li) 

li=[20,10,40,30,50]  
a=rev_list(li)     

# Method 2:
def reverse(li):
    print(li[::-1])

li=[20,10,40,30,50] 
reverse(li)    