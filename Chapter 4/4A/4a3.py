import os
os.system('cls||clear')

# Code starts here

month_number = int(input())

if month_number == 2:
  days = "28 or 29 days"
elif month_number % 2 == 0:
  if month_number < 7:
    days = "30 days"
  if month_number > 7:
    days = "31 days"
elif month_number % 2 == 1:
  if month_number <= 7:
    days = "31 days"
  if month_number > 7:
    days = "30 days"

print(days)
  
# -------Days in a month--------
#The length of a month varies from 28 to 31 days. In this exercise you will create a program that reads the
# month number from the user. Then your program should display the number of days in that month. 
# Display “28 or 29 days” for an input of 2 (February) so that leap years are addressed.
#Note: Please use modulo(%) as part of your solution.
