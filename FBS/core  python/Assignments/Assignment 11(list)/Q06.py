### Q6. Python Program to Find the Union of two Lists ?

def duplicate_remover(li):
    
    new = []
    new1= []

    for ele in li:
        count = 0

        for i in li:
            if ele == i:
                count += 1

        if count == 1:
            
            new += [ele]
        elif count >= 2:
            if ele not in new1:
                new1 += [ele]
            
    li= new + new1
    return li
