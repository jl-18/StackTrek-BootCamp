import os
os.system('cls||clear')

# Code starts here
year = int(input())

if (year - 2000) % 12 == 0:
  sign = "Dragon"
elif (year - 2000) % 12 == 1:
  sign = "Snake"
elif (year - 2000) % 12 == 2:
  sign = "Horse"
elif (year - 2000) % 12 == 3:
  sign = "Sheep"
elif (year - 2000) % 12 == 4:
  sign = "Monkey"
elif (year - 2000) % 12 == 5:
  sign = "Rooster"
elif (year - 2000) % 12 == 6:
  sign = "Dog"
elif (year - 2000) % 12 == 7:
  sign = "Boar"
elif (year - 2000) % 12 == 8:
  sign = "Rat"
elif (year - 2000) % 12 == 9:
  sign = "Ox"
elif (year - 2000) % 12 == 10:
  sign = "Tiger"
else:
  sign = "Hare"
  
print(sign)


#-----Chinese Zodiac-----
#"""The Chinese zodiac assigns animals to years in a 12 year cycle. One 12 year cycle is shown in the table 
# below. The pattern is repeated with 2012 being another year of the dragon, and 1999 being another year of 
# the hare.
#Write a program that reads a year from the user and displays the animal associated with that year. 
# Your program should work correctly for any year greater than or equal to zero, not just the ones listed in 
# the table."""
