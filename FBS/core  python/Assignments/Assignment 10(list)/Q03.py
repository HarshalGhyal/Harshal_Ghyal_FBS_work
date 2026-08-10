#### Q3.3. Write a program to find the second largest element in the list.

def sec_larges(li):
    max=li[0]
    for ind in range(1,len(li)):
        if li[ind]>max:
            max=li[ind]
    s_max=max-li[0]
    # as we know diifrence betn largest and second largest is minimum compare to other elements:
    for ind in range(1,len(li)):
        if s_max> max-li[ind] and max-li[ind]!=0:
            iind=ind
            s_max=max-li[ind]
    second_largest=max-s_max
    print(f"Second largest number in list: {second_largest}  index of second largest: {iind}")  

li=[300,400,500,235,3004,2301,4531,879]
sec_larges(li)    
