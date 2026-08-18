
def sec_largest(li):
    # lets find largest number first:
    max=li[0]
    for ind in range(1,len(li)):
        if li[ind]>max:
            max=li[ind]
   # as we know diifrence betn largest and second largest is minimum compare to other elements:
    s_max=max-li[0]
    for ind in range(1,len(li)):
        if s_max> max-li[ind] and max-li[ind]!=0:
            s_max=max-li[ind]
    second_largest=max-s_max
    print("second largest number in list :",second_largest) 


def lis_creation():
    n=int(input("enter number of elements:"))
    li=[]
    for i in range(1,n+1):
        num=int(input(f"Enter number {i}:"))
        li+=[num]   
    return li
                
li=lis_creation()  
sec_largest(li)  
