try:
    def add(a,b):
        return a+b
except TypeError as e:
    print(e)  
except Exception as s:
    print(s)
finally:
    print('code is executed')     


# I have to add except here not for all for function

a=add('s',3)    
print(a)