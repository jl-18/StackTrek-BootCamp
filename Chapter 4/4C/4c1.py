import os
os.system('cls||clear')

# Code starts here

from math import sqrt

A = float(input())
B = float(input())
C = float(input())

square = abs((B ** 2) - (4 * A * C))
sol1 = (-B + sqrt(square)) / (2 * A)
sol2 = (-B - sqrt(square)) / (2 * A)

if A == 0 and B == 0:
  solution = "There is not even an unknown in this equation!"
  
if (B ** 2) - (4 * A * C) > 0:
  solution = (f"There are two solutions , namely {sol1} and {sol2}")
  
if (B ** 2) - (4 * A * C) == 0:
  solution = (f"There is one solution , namely {sol1}")
  
if (B ** 2) - (4 * A * C) < 0:
  solution = "There are no solutions"

print(solution)

#Grades are values between zero and 10 (both zero and 10 included), and are always rounded to the 
# nearest half point.
#To translate grades to the American style, 8.5 to 10 become an “A”, 7.5 and 8 become a “B”, 6.5 and 7 
# become a “C”, 5.5 and 6 become a “D”, and other grades become an “F”.
#Implement this translation, whereby you ask the user for a grade, and then give the American translation. 
# If the user enters a grade lower than zero or higher than 10, just give an error message. 
# You do not need to handle the user entering grades that do not end in .0 or .5, though you may do that 
# if you like – in that case, if the user enters such an illegal grade, give an appropriate error message.
