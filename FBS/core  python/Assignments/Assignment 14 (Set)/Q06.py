#### Q6.Write a Python program to find the two numbers whose product is
# maximum among all the pairs in a given list of numbers. Use the
# Python set.


li=[6,1,3,7,9,12,4,7]
def max_product_pair(li):
    max=li[0]*li[1]
    pairs=[]
    for i in range(2,len(li)):
        for j in range(i+1,len(li)):
            if li[i]*li[j]>max:
                max=li[i]*li[j]
                pairs=(li[i],li[j])
    return set(pairs)            

res=max_product_pair(li)
print(res)
           