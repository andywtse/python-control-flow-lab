# exercise-06 What's the  Season?

# Write the code that:
# 1. Prompts the user to enter the month (as three characters):
#      Enter the month of the year (Jan - Dec):
# 2. Then prompts the user to enter the day of the month: 
#      Enter the day of the month:
# 3. Calculate what season it is based upon this chart:
#      Dec 21 - Mar 19: Winter
#      Mar 20 - Jun 20: Spring
#      Jun 21 - Sep 21: Summer
#      Sep 22 - Dec 20: Fall
# 4. Print the result as follows:
#      <Mmm> <dd> is in <season> 

# Hints:
# Consider using the in operator to check if a string is in a particular list/tuple like this:
# if input_month in ('Jan', 'Feb', 'Mar'):
#
# After setting the likely season, you can use another if...elif...else statement to "adjust" if
# the day number falls within a certain range.

my_month = input("Enter the month of the year (Jan - Dec): ")
my_day = int(input("Enter the day of the month:"))

monthList = {
  "Jan":0, 
  "Feb":31, 
  "Mar":59, 
  "Apr":90, 
  "May":120, 
  "Jun":151, 
  "Jul":181, 
  "Aug":212, 
  "Sep":243, 
  "Oct":273, 
  "Nov":304, 
  "Dec":334
  }

spring = range(79, 172)
summer = range(172, 264)
fall = range(264, 355)

season = ''

for month in monthList:
  if(my_month == month):
    sum = monthList.get(my_month) + my_day
    if( sum in spring ):
      season = 'Spring'
    elif( sum in summer ):
      season = 'Summer'
    elif( sum in fall ):
      season = 'Fall'
    else:
      season = "Winter"

print(f'{my_month} {my_day} is in {season}')