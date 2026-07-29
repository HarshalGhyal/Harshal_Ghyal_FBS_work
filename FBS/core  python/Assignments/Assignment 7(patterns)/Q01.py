#### Q1.print following pattern:
#           *         
#        *    *       
#      *        *     
#    *            *   
#  *                * 
#  *                * 
#    *            *   
#      *        *     
#        *    *       
#          *         




#start:
for i in range(1,11):
    
    for j in range(1,10):
        if i+j==6 or j-i==4 or i+j==15 or i-j==5:
            print(" *",end=" ") 
        else:
            print(" ",end=" ")
    print()               
    
