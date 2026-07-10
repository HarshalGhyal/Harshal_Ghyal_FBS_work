#### Q8. write a program to calculate years ,weeks and days by given days as input from user.

# input days you want to convert into years,weeks and days.
g_days=int(input("enter your days:"))

# lets calculate years
years=g_days//365

#lets calculate remaining days that not fit to be a year.
r_days=g_days%365

#lets calculate weeks out of remaining days by dividing with 7.
week=r_days//7

#lets calulate remaining days or days that are not fit to be a week. 
days=r_days%7

#lets display the output
print(f"Years: {years}, Weeks: {week}, Days: {days}")
