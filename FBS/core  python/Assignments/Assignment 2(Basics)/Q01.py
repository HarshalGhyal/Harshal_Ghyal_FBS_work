#### Q1.Convert the time entered in hh,min and sec into seconds.

hh = int(input("Enter hours: "))

#As we know 1 hour = 3600 seconds, we will multiply the hours by 3600 to convert it into seconds.
hh_in_sec = hh * 3600

#As we know 1 hour=60 minutes ,so we will multiply hours by 60 to convert it into minutes.
hh_in_min=hh*60

#lets display the output

print(f"hours:{hh} , Minutes:{hh_in_min} , seconds:{hh_in_sec}")