### Q8. Print 1 to 100 in snakes and ladder pattern ?

start = 100
end = 90

li = []

for j in range(10):
    row = []

    for i in range(start, end, -1):
        row += [i]

    li += [row]

    start = end
    end = start - 10

print(li)