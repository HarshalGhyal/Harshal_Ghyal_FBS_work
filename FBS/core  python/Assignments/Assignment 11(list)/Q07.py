### Q7. Python Program to Find the Intersection of Two Lists ?

def repeated_num(li):
    new = []


    for ele in li:
        count = 0

        for i in li:
            if ele == i:
                count += 1

            # if count == 1:
                
            #     new += [ele]
            if count >= 2:
                if ele not in new:
                    new += [ele]
    return new    
  
def intersection(li1, li2):
    li = []     
    li = li1 + li2
    
    li = repeated_num(li)
    
    return li

li = [12, 45, 56, 89, 112] 
li2 = [10, 56, 45, 89, 90]  

res=intersection(li, li2) 
print(res)
                
        
        

