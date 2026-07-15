#### Q11. Accept age of five people and also per person ticket amount and then calculate total
# amount to ticket to travel for all of them based on following condition :
# a. Children below 12 = 30% discount
# b. Senior citizen (above 59) = 50% discount
# c. Others need to pay full.

# lets accept ticket price first:
actual_T_price=float(input("Enter ticket price:"))

# lets take total amt of ticket for 5 person is 0:
total_amt=0
# lets accept age of 5 persons as p1,p2,p3 etc.

p1=int(input("Enter the age of person 1:"))
p2=int(input("Enter the age of person 2:"))
p3=int(input("Enter the age of person 3:"))
p4=int(input("Enter the age of person 4:"))
p5=int(input("Enter the age of person 5:"))

# lets check what ticket price they have to pay according to their age so we have check seperately for every person:

#for person 1 that is p1
if(p1<12 ):
    tic_p_for_p1=actual_T_price-(actual_T_price*30/100)
    print(f'\nticket price for person 1 is {tic_p_for_p1}')
    total_amt+=tic_p_for_p1
elif(p1>59):
     tick_p_for_p1=actual_T_price-(actual_T_price*50/100)
     print(f'\nticket price for person 1 is {tick_p_for_p1}')
     total_amt+=tick_p_for_p1
else:
     print(f'\nticket price for person 1 is {actual_T_price}')
     total_amt+=actual_T_price
# for person 2 that is p2
if(p2<12 ):
    tic_p_for_p2=actual_T_price-(actual_T_price*30/100)
    print(f'ticket price for person 2 is {tic_p_for_p2}')
    total_amt+=tic_p_for_p2
elif(p2>59):
     tick_p_for_p2=actual_T_price-(actual_T_price*50/100)
     print(f'ticket price for person 2 is {tick_p_for_p2}')
     total_amt+=tick_p_for_p2
else:
     print(f'ticket price for person 2 is {actual_T_price}')
     total_amt+=actual_T_price
# for person 3 that is p3
if(p3<12 ):
    tic_p_for_p3=actual_T_price-(actual_T_price*30/100)
    print(f'ticket price for person 3 is {tic_p_for_p3}')
    total_amt+=tic_p_for_p3
elif(p3>59):
     tick_p_for_p3=actual_T_price-(actual_T_price*50/100)
     print(f'ticket price for person 3 is {tick_p_for_p3}')
     total_amt+=tick_p_for_p3
else:
     print(f'ticket price for person 3 is {actual_T_price}')
     total_amt+=actual_T_price
# for person 4 that is p4
if(p4<12 ):
    tic_p_for_p4=actual_T_price-(actual_T_price*30/100)
    print(f'ticket price for person 4 is {tic_p_for_p4}')
    total_amt+=tic_p_for_p4
elif(p4>59):
     tick_p_for_p4=actual_T_price-(actual_T_price*50/100)
     print(f'ticket price for person 4 is {tick_p_for_p4}')
     total_amt+=tick_p_for_p4
else:
     print(f'ticket price for person 4 is {actual_T_price}')
     total_amt+=actual_T_price
# for person 5 that is p5
if(p5<12 ):
    tic_p_for_p5=actual_T_price-(actual_T_price*30/100)
    print(f'ticket price for person 5 is {tic_p_for_p5}')
    total_amt+=tic_p_for_p5
elif(p5>59):
     tick_p_for_p5=actual_T_price-(actual_T_price*50/100)
     print(f'ticket price for person 5 is {tick_p_for_p5}')
     total_amt+=tick_p_for_p5
else:
     print(f'ticket price for person 5 is {actual_T_price}')
     total_amt+=actual_T_price

print(f'the total amount of ticket price for all 5 person is {total_amt}')

          


