#### Q12.12. Write a program to check if given number is Armstrong number or not.
# (Hint : 153 = 1*1*1 + 5*5*5 + 3*3*3 , 1634 = 1*1*1*1 + 6*6*6*6 + 3*3*3*3 +
# 4*4*4*4)


#lets take input as a num
num=int(input("Enter number:"))
#lets put num in temp
temp=num
#lets calculate length of number which very imp for exponant count .to calculate length we have to dt of num to str and then vice versa.
num=str(num)
l=len(num)
num=int(num)

#lets initalize var sum 
sum=0

#lets iterating with while for seperating digits.
while(num>0):
    d=num%10
    mul=d**l
   #lets add every multiplication of sep digit in sum
    sum=sum+mul
    # move on to find next sep digit
    num=num//10

#lets compare for armstong number
if temp==sum:
    print(f"{temp} is armstrong number !")
else:
     print(f"{temp} is not armstrong number !")         



