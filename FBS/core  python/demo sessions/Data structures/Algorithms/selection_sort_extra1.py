def min_index(li, start):
    min = li[start]
    min_ind = start

    for ind in range(start + 1, len(li)):
        if li[ind] < min:
            min = li[ind]
            min_ind = ind

    return min_ind


def selection_sort(li):
    for i in range(len(li) - 1):
        min_ind = min_index(li, i)
        li[i], li[min_ind] = li[min_ind], li[i]


li = [60, 50, 40, 30, 20, 10]

print("Before sorting:", li)

selection_sort(li)

print("After sorting :", li)