#### Q5. Accept a number from user and check if this element is present in the list or
# not. Also tell how many times it is present in the list.


def is_present(li,ele):
    count=0
    if ele in li:
        for i in li:
            if ele==i:
                count+=1
                
        print(f"{ele} is present in given list {count} times")
    else:
        print(f"{ele} is not present in given list")    

li=[20,10,20,30,50,40,70,10]
is_present(li,20)        