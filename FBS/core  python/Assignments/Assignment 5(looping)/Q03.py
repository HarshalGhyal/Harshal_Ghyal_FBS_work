#### Q3.Accept no. of passengers from user and per ticket cost. Then accept age of each
# passenger and then calculate total amount to ticket to travel for all of them based on
# following condition :
# a. Children below 12 = 30% discount
# b. Senior citizen (above 59) = 50% discount
# c. Others need to pay full.

# lets take no. of passegers as a input
n_pasg=int(input("Enter No. of passengers:"))

# let initialize total_amt var
total_amt=0
for i in range(1,n_pasg+1):
    Tic_cost=int(input(f"Enter ticket cost for passenger {i}:"))
    age=int(input(f"Enter age of passenger {i}:"))

    if(age<12):    
        Tic_cost=Tic_cost-(Tic_cost*30/100)
        print(f'\nticket price for person {i} is {Tic_cost}')
        
    elif(age>59):
        Tic_cost=Tic_cost-(Tic_cost*50/100)
        print(f'ticket price for person {i} is {Tic_cost}')
      
    else:
        print(f'ticket price for person {i} is {Tic_cost}')
    total_amt+=Tic_cost

else:
    print(f"total amount of cost of ticket for all given passengers is {total_amt}")    


       