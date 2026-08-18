def min_max(li):
    min=li[0]
    max=li[0]
    for ind in range(1,len(li)):
            if li[ind]<min:
                min=li[ind]
            elif li[ind]>max:
                max=li[ind]   
        
    return min,max
    # print("max:",max) 
    # print("min:",min)   

li=[10,9,1,31,46]
print(type(min_max(li)))

# Q. if im returning min,max why answer coming in bracket