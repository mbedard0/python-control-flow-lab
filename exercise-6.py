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

winter_edge_months = ['Dec', 'Mar']
winter_months = ['Jan', 'Feb']
spring_edge_months = ['Mar', 'Jun']
spring_months = ['Apr', 'May']
summer_edge_months = ['Jun', 'Sep']
summer_months = ['Jul', 'Aug']
fall_edge_months = ['Sep', 'Dec']
fall_months = ['Oct', 'Nov']

winter_mar_days = range(1, 20)
twenty_one_days = range(21, 32)
twenty_days = range(20, 31)
twenty_beginning_days = range(1, 21)
twenty_one_beginning_days = range(1, 22)
sep_fall_days = range(1, 23)
# up_to_twenty_one_days = 
# spring_days = []
# summer_days = []
# fall_days = []

month = input('Enter the month of the year (Jan - Dec):')
day = int(input('Enter the day of the month:'))

# if month in winter_months and day in winter_days:
#   print(f'{month} {day} is in Winter')

if month in winter_months or month in winter_edge_months:
  if month in winter_months == winter_months:
    print(f'{month} {day} is in winter')
  elif month == 'Dec' and day in twenty_one_days:
    print(f'{month} {day} is in winter')
  elif month == 'Mar' and day in winter_mar_days:
    print(f'{month} {day} is in winter')

if month in spring_months or month in spring_edge_months:
  if month in spring_months == spring_months:
    print(f'{month} {day} is in Spring')
  elif month == 'Mar' and day in twenty_days:
    print(f'{month} {day} is in Spring')
  elif month == 'Jun' and day in twenty_beginning_days:
    print(f'{month} {day} is in Spring')

if month in summer_months or month in summer_edge_months:
  if month in summer_months == summer_months:
    print(f'{month} {day} is in Summer')
  elif month == 'Jun' and day in twenty_one_days:
    print(f'{month} {day} is in Summer')
  elif month == 'Sep' and day in twenty_one_beginning_days:
    print(f'{month} {day} is in Summer')

if month in fall_months or month in fall_edge_months:
  if month in fall_months == fall_months:
    print(f'{month} {day} is in Fall')
  elif month == 'Jun' and day in sep_fall_days:
    print(f'{month} {day} is in Fall')
  elif month == 'Sep' and day in twenty_beginning_days:
    print(f'{month} {day} is in Fall')