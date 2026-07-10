#### Q10.Write a program to reverse three-digit number.

## Method 1:

#lets take input as three digit number:

num=int(input("Enter three digit number:"))

# for last digit:
d1=num%10
#for first two digit:
a2=num//10
#for middle digit
d2=a2%10
#for first digit
d3=a2//10

#now we take var as reverse num as r_num:
# as we know digit place and its value lets multiply them with its place value and add them to get our reverse three digit number.

r_num=d1*100+d2*10+d3*1

#lets print output

print(f'before reversing: {num} , after reversing: {r_num}')


## Method 2:

#lets take input as three digit number:
number=int(input("Enter three digit number:")) # or we can take input as string only.

#lets convert it to string.
number=str(number)

#lets reverse the string:
R_number=number[::-1]

#lets convert it to integer.
R_number=int(R_number)

# lets print output:

print(f'before reversing: {number} , after reversing: {R_number}')




