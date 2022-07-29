import os
os.system('cls||clear')

# Code starts here

age = input()
price = 0

while (age != "end"):
  a = int(age)
  if a <= 2:
    price += 0
  elif (a >= 3) and (a <= 12):
    price += 14
  elif a >= 65:
    price += 18
  else:
    price += 23
  age = input()
    
    
print(f"{price:.2f}")
  
#---- Admisiion Price-----
#A particular zoo determines the price of admission based on the age of the guest. Guests 2 years of age
#  and less are admitted without charge. Children between 3 and 12 years of age cost $14.00. Seniors aged
#  65 years and over cost $18.00. Admission for all other guests is $23.00.
#Create a program that begins by reading the ages of all of the guests in a group from the user, with one
#  age entered on each line. The user will enter end to indicate that there are no more guests in the group. 
# Then your program should display the admission cost for the group. The cost should be displayed using 
# exactly two decimal places.
