#### Q4.print following pattern.
#         1 
#       2 3 2 
#     3 4 5 4 3 
#   4 5 6 7 6 5 4 
# 5 6 7 8 9 8 7 6 5 


#start:


for i in range(1,6):
    for j in range(5-i,0,-1):
        print(" ",end=" ")
    num=i
    for j in range(1,i+1):
        print(num,end=" ")  
        num+=1
    k=(i-1)*2
    for j in range(1,i):
         print(k,end=" ")  
         k-=1
    print()          