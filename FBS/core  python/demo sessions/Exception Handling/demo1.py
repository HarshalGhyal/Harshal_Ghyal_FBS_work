try:
    num1=int(input("Enter number 1:"))
    num2=int(input("Enter number 2:"))
    print(num1//num2)
except ZeroDivisionError as e:
    print(e)    
except ValueError as z:
    print('Enter proper integer value')  
except Exception as v:
    print("Cannot divided by zero")  
else:
    print("Code execute successfully without exception !")