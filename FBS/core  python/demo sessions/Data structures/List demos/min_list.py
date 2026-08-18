# code to find minimum element in list:

def min_list(li):
    min=li[0]
    for ind in range(1,len(li)):
        if li[ind]<min:
            min=li[ind]
    return min

li=[59089,58004,56067,59345]  
res=min_list(li)  
print(res)    