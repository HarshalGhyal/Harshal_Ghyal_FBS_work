# A A A A A
# B B B B B
# C C C C C
# D D D D D
# E E E E E 




# step1:
# s="abcde"
# for i in s:
#     for j in s:
#         print(i,end=" ")
#     print() 

#step2:
# a=65
# for i in range(1,6):
#     for j in range(1,6):
#         print(chr(a),end=' ')
#     print()
#     a+=1 
      

#step 3:
for i in range(1,6):
    for j in range(1,i+1):
        print(chr(64+j),end=' ')
    print()
    
      