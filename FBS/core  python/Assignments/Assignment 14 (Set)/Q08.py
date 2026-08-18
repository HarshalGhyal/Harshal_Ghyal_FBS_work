#### Q8.Write a Python program to find all the anagrams and group them
# together from a given list of strings.

li=['listyuien','listen','silent','ittslent','listent']
def anagram_list(li):
    li2=[]
    li3=[]
    li4=[]

    for i in li:
        li2.append(sorted(i))

    for j in range(len(li2)):
        for k in range(j+1, len(li2)):
            if li2[j] == li2[k]:
                li3.append(li2[j])

    for c in li3:
        for i in range(len(li2)):
            if c == li2[i]:
                li4.append(li[i])

    print(set(li4))
anagram_list(li)                       