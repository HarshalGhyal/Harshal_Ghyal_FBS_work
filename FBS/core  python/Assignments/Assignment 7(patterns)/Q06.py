#### Q6.print following pattern:
# 1 2 3 4 5 
# 2     5 
# 3   5 
# 4 5 
# 5 


for i in range(1,6):
    
    for j in range(i,6):
        if j==i or j==5 or i==1 :
            print(j,end=" ")
        else :
            print(" ",end=" ") 
    print()
    
            
           
    

    
    
        
            
           



    