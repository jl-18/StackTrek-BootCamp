import os
os.system('cls||clear')

# Code starts here

magnitude = float(input())

if magnitude < 2:
  description = "Micro"
elif 2 <= magnitude < 3:
  description = "Very minor"
elif 3 <= magnitude < 4:
  desctiption = "Minor"
elif 4 <= magnitude < 5:
  description = "Light"
elif 5 <= magnitude < 6:
  description = "Moderate"
elif 6 <= magnitude < 7:
  description = "Strong"
elif 7 <= magnitude < 8:
  description = "Major"
elif 8 <= magnitude < 9:
  description = "Great"
else:
  description = "Meteoric"
  
print(description)


# ------Quake-------
# Write a program that reads a magnitude from the user and displays the appropriate descriptor as part of a 
# meaningful message. For example, if the user enters 5.5 then your program should indicate that a magnitude 
# 5.5 earthquake is considered to be a Moderate earthquake.
