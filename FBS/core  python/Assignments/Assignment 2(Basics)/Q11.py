#### Q11.Write a program to accept an integer amount from user and tell minimum number of notes needed for representing that amount.

# lets take input as amount as var amt.

amt=int(input("enter your amount:"))

# lets calculate how many rupees 500 hunderd notes needed and reamining amount that cannot fullfill by 500 note.
five_h_notes=amt//500

r_amt_tofullfill=amt%500

#now for  rupees 100 notes needed and reamining amount that cannot fullfill by 100 note.
one_h_notes=r_amt_tofullfill//100

rr_amt_fullfill=r_amt_tofullfill%100

#now for rupees 50 notes needed and reamining amount that cannot fullfill by 50 note.
fifty_notes=rr_amt_fullfill//50

rrr_amt_fullfill=rr_amt_fullfill%50

#now for rupees 10 notes needed and reamining amount that cannot fullfill by  note.

ten_notes=rrr_amt_fullfill//10

# now print the output:

print(f'for amount:{amt}, 500 notes:{five_h_notes}, 100 notes:{one_h_notes}, 50 notes:{fifty_notes}, 10 notes:{ten_notes}')