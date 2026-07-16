#### Q11. Accept age of five people and also per person ticket amount and then calculate total
# amount to ticket to travel for all of them based on following condition :
# a. Children below 12 = 30% discount
# b. Senior citizen (above 59) = 50% discount
# c. Others need to pay full.

# lets accept ticket price first:
T_price_p1=float(input("Enter ticket price of person 1:"))
T_price_p2=float(input("Enter ticket price of person 2:"))
T_price_p3=float(input("Enter ticket price of person 3:"))
T_price_p4=float(input("Enter ticket price of person 4:")) 
T_price_p5=float(input("Enter ticket price of person 5:"))

# lets take total amt of ticket for 5 person is 0:
total_amt=0
# lets accept age of 5 persons as p1,p2,p3 etc.

p1=int(input("\nEnter the age of person 1:"))
p2=int(input("Enter the age of person 2:"))
p3=int(input("Enter the age of person 3:"))
p4=int(input("Enter the age of person 4:"))
p5=int(input("Enter the age of person 5:"))

# lets check what ticket price they have to pay according to their age so we have check seperately for every person:

#for person 1 that is T_price_p4
if(p1<12):    
    tic_p_for_p1=T_price_p1-(T_price_p1*30/100)
    print(f'\nticket price for person 1 is {tic_p_for_p1}')
    total_amt+=tic_p_for_p1
elif(p1>59):
     tick_p_for_p1=T_price_p1-(T_price_p1*50/100)
     print(f'\nticket price for person 1 is {tick_p_for_p1}')
     total_amt+=tick_p_for_p1
else:
     print(f'\nticket price for person 1 is {T_price_p1}')
     total_amt+=T_price_p1

# for person 2 that is p2
if(p2<12 ):
    tic_p_for_p2=T_price_p2-(T_price_p2*30/100)
    print(f'ticket price for person 2 is {tic_p_for_p2}')
    total_amt+=tic_p_for_p2
elif(p2>59):
     tick_p_for_p2=T_price_p2-(T_price_p2*50/100)
     print(f'ticket price for person 2 is {tick_p_for_p2}')
     total_amt+=tick_p_for_p2
else:
     print(f'ticket price for person 2 is {T_price_p2}')
     total_amt+=T_price_p2

# for person 3 that is p3
if(p3<12 ):
    tic_p_for_p3=T_price_p3-(T_price_p3*30/100)
    print(f'ticket price for person 3 is {tic_p_for_p3}')
    total_amt+=tic_p_for_p3
elif(p3>59):
     tick_p_for_p3=T_price_p3-(T_price_p3*50/100)
     print(f'ticket price for person 3 is {tick_p_for_p3}')
     total_amt+=tick_p_for_p3
else:
     print(f'ticket price for person 3 is {T_price_p3}')
     total_amt+=T_price_p3

# for person 4 that is p4
if(p4<12 ):
    tic_p_for_p4=T_price_p4-(T_price_p4*30/100)
    print(f'ticket price for person 4 is {tic_p_for_p4}')
    total_amt+=tic_p_for_p4
elif(p4>59):
     tick_p_for_p4=T_price_p4-(T_price_p4*50/100)
     print(f'ticket price for person 4 is {tick_p_for_p4}')
     total_amt+=tick_p_for_p4
else:
     print(f'ticket price for person 4 is {T_price_p4}')
     total_amt+=T_price_p4

# for person 5 that is p5
if(p5<12 ):
    tic_p_for_p5=T_price_p5-(T_price_p5*30/100)
    print(f'ticket price for person 5 is {tic_p_for_p5}')
    total_amt+=tic_p_for_p5
elif(p5>59):
     tick_p_for_p5=T_price_p5-(T_price_p5*50/100)
     print(f'ticket price for person 5 is {tick_p_for_p5}')
     total_amt+=tick_p_for_p5
else:
     print(f'ticket price for person 5 is {T_price_p5}')
     total_amt+=T_price_p5

print(f'the total amount of ticket price for all 5 person is {total_amt}')

          






