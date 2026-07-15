#### Q2.Write a program to input any alphabet and check whether it is vowel or consonant.

# lets take input as a character that describes a alphabet:

char=input("enter a alphabet:")

# lets check whether its a vowel or consonant.
if char.isalpha() and len(char)==1 :
    if char=='a' or char=='e' or char=='i' or char=='o' or char=='u'or char=='A' or char=='E' or char=='I' or char=='O' or char=='U':
        print("given alphabet is vowel")
    else:
        print(" given alphabet is consonant") 

else:
    print("enter appropriate input!")           