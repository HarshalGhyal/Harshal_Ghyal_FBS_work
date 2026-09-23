try:
    num1=int(input('Enter number 1:'))
    num2=int(input('Enter number 2:'))
    if num2<=0:
        raise ValueError('num2 should be greater than 0 !')
    else:
        print(num1//num2)
except Exception as e:
    print(e)
