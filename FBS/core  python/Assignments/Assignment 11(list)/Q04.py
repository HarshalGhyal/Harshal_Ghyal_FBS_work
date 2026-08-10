### Q4. Python Program to Find the Second Largest Number in a List Using Bubble sort

def bubble_Sort_sec_largest (li):
    size = len (li)
    
    for i in range (1, size):
        for j in range (0, size - i):
            if (li[j] > li[j + 1]):
                li[j], li[j + 1] = li[j + 1], li[j]
    second_largest = li[len(li) - 2]
    
    print(f"second largest in given list is {second_largest}")
    
li = [30, 50, 67, 89, 12, 45]

bubble_Sort_sec_largest(li)