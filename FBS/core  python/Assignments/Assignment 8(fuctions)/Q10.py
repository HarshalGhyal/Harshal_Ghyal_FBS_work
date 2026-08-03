#### Q10. Write a program to check if entered year is a leap year or not.

def is_leap(year):
    
    if  year%400==0:
        return f"{year} is leap year !"
    elif year%100==0:
        return f"{year} is not a leap year !"
    elif year%4==0 :
        return f"{year} is leap year !"
    else:
        return f"{year} is not a leap year !"
    

year = int(input("Enter year to check leap year or not:"))
c=is_leap(year)
print(c)