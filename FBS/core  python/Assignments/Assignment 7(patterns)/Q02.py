#### Q2.print following pattern:
# * 
# * * 
# * * * 
# * * * * 
# * * * * * 
# * * * * 
# * * * 
# * * 
# * 

#start:
for i in range(1,6):
    for j in range(1,i+1):
        print('*',end=" ")
    print() 
for i in range(1,5):    
    for j in range(5-i,0,-1):  
        print("*",end=" ") 
    print()    