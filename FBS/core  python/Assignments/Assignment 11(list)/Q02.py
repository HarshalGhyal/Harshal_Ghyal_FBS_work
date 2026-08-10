#### Q2. Python Program to Merge Two Lists and Sort it.

def two_list_merge_and_sort(li1,li2):
    li=[]
    li=li1+li2
    li.sort()
    print(li)

li1=[9,8,7,6,5]    
li2=[4,3,2,1]
two_list_merge_and_sort(li1,li2)