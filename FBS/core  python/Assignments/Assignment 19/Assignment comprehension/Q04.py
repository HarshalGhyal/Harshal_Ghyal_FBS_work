#### 4. Remove all of the vowels in a string (take input from user)

st=input('Enter String:')

li=[i for i in st.lower() if i not in 'aeiou']
print(''.join(li))
 