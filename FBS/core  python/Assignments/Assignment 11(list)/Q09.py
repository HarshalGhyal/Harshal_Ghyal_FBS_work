### Q9. Write a program to create three lists of numbers, their squares and cubes ?

def create_list(li):
    square = []
    cube = []
    
    for val in li :
        square.append( val * val)
        cube.append( val * val * val )
        
    return li, square, cube

li = [1, 2, 3, 4, 5]
li, square, cube = create_list(li)

print(f"It is a list :", li)
print(f"It is a square :", square)
print(f"It is a cube :", cube)