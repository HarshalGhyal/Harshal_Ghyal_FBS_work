#### Q5.Python Program to Count the Number of Vowels in a String.

def count_vowels(str):
    vowel='aeiou'
    count=0

    for i in vowel:
        for j in str:
            if i==j:
                count+=1
    return f'count of vowels in given string is {count}'   


st='harshal is good boy'
res=count_vowels(st)
print(res)
         
    
           