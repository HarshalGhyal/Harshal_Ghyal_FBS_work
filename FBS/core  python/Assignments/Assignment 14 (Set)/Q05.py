#### Q5. Write a Python program to find the longest common prefix of all strings. Use the Python set.

s = ['python', 'pycharm', 'pyramid']

word = s[0]
prefix = ''

for i in range(len(word)):
    st = set()

    for j in s:
        st.add(j[i])

    if len(st) == 1:
        prefix += word[i]
    else:
        break

print(prefix)