#### Q7. Given two sets of numbers, write a Python program to find the missing
# numbers in the second set as compared to the first and vice versa.
# Use the Python set.
s={1,2,3,4,5}
s1={3,4,5,6,7,8}
def compare_two_sets(s,s1):
    li=[]
    li2=[]
    for i in s:
        if i not in s1:
            li+=[i]
    print(f'Missing element in set 2 compare to set1:{set(li)}') 
    for j in s1:
        if j not in s:
            li2+=[j]    
    print(f'Missing element in set1 compare to set2:{set(li2)}')        

compare_two_sets(s,s1)