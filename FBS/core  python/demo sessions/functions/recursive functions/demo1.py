
def series(n):
    
    if n>0:
        print(n)
        
        return n + series(n-1) 
    else:
        return 0   
    
n=5
a=series(n)  
print(a)  