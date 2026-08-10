#### Q2. Write a program to find maximum and minimum element in a list.

def min_max(li):
    min=li[0]
    max=li[0]
    for ind in range(1,len(li)):
            if li[ind]<min:
                min=li[ind]
                index_min=ind
            elif li[ind]>max:
                max=li[ind]   
                index_max=ind
    
    print(f"maximum element is {max} it is at index {index_max} of given list !") 
    print(f"minimum element is {min} it is at index {index_min} of given list !") 
li=[10,9,1,31,46]
min_max(li)