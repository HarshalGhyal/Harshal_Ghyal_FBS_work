#### Q3.print following pattern(pascal triangle):

#         1 
#       1   1 
#     1   2   1 
#   1   3   3   1 



from math import factorial
n=int(input("Enter number of rows:"))

for i in range(n):
    for j in range((n-1)-i,0,-1):
        print(" ",end=" ")

    for j in range(i+1):
        ncr=factorial(i)//(factorial(j)*factorial(i-j))
        print(" ",ncr,end=" ")



    print()
