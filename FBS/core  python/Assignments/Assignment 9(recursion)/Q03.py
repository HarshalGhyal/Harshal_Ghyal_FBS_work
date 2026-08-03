#### Q3.Write a program to reverse a given number using recursive function.

def rev(num):
    
    if num>0:
        digit=num%10
        
        print(digit,end="")
        rev(num//10)

        
num=int(input("Enter number:"))
rev(num)

   


   



    



