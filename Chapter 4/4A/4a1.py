import os
os.system('cls||clear')

# Code starts here

human = int(input())
first_two = 2 * 10.5
additional = (human - 2) * 4
human_years = first_two + additional
if human_years <= 2:
  print(float(human_years))
else:
  print(int(human_years))



# ---------DOG YEARS-------
# """It is commonly said that one human year is equivalent to 7 dog years.
#  However, this simple conversion fails to recognize that dogs reach adulthood in approximately two years. 
# As a result, some people believe that it is better to count each of the first two human years as 
# 10.5 dog years, and then count each additional human year as 4 dog years.
# Write a program that implements the conversion from human years to dog years.
# The program will accept the number of human years (integer) as the user's input.
# The program should output the converted number of dog years.
#If the number of human years is less than or equal to 2, output a float (multiple of 10.5).
#If the number of human years is greater than 2, output an integer"''"
