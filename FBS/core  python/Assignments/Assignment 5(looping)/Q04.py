#### Q4.WAP to print Armstrong number within a given range.

# lets take input as start and end.
start=int(input("Enter starting number:"))
end=int(input("Enter ending number:"))

# lets iterate from start to end numbers
for i in range(start,end+1):
    # lets save i value in temp to use it as number provided
    temp=i
    # lets calculate length of number to give exponent
    l=len(str(i))
    #lets initialize sum var inside loop so it becomes zero after 1 iteration.
    sum=0
    while(temp>0):
        d=temp%10
        mul=d**l
        #lets add every multiplication of sep digit in sum
        sum=sum+mul
        # move on to find next sep digit
        temp=temp//10    
    # now check  is given no. armstrong or not if it is print it.
    if sum==i:
        print(i)
    



