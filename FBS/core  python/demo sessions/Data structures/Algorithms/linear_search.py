def linear_search(li,search_ele):
    for ind in range(0,len(li)):
        if(li[ind]==search_ele):
            return ind
    else:
        return -1


ele=int(input("Enter num to find:")) 
li=[69,45,67,45,78,34,90]       
res=linear_search(li,ele)

if(res!=-1):
    print(f"{ele} is present at index {res}")
else:
    print(f"{ele} is not present in list")    