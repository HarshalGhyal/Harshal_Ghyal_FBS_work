def selection_sort(li):
    size=len(li)
    for i in range(0,size-1):
        max_ind=i
        for j in range(i+1,size):
            if(li[j]>li[max_ind]):
                max_ind=j
        li[i],li[max_ind] =li[max_ind],li[i]  
    print(li)     
li=[40,50,60,20,30,10]
print("before sorting:",li)
print("\nAfter sorting:")
selection_sort(li)
