import os
os.system('cls||clear')

# Code starts here

grade_value = float(input())

if (grade_value >= 0.0) and (grade_value <= 10.0):
  if (grade_value % 1 != 0.5) and (grade_value % 1 != 0.0):
    grade = "Grades should be rounded to the nearest half point."
  elif (grade_value >= 8.5) and (grade_value <= 10):
    grade = "Grade A"
  elif (grade_value >= 7.5) and (grade_value <= 8):
    grade = "Grade B"
  elif (grade_value >= 6.5) and (grade_value <= 7):
    grade = "Grade C"
  elif (grade_value >= 5.5) and (grade_value <= 6):
    grade = "Grade D"
  elif (grade_value >= 0) and (grade_value < 5.5):
    grade = "Grade F"
else:
    grade = "Grades should be between zero and 10."
print(grade)

#-----American Grades----
#Grades are values between zero and 10 (both zero and 10 included), and are always rounded to the nearest 
# half point.
#To translate grades to the American style, 8.5 to 10 become an “A”, 7.5 and 8 become a “B”, 6.5 and 7 
# become a “C”, 5.5 and 6 become a “D”, and other grades become an “F”.
#Implement this translation, whereby you ask the user for a grade, and then give the American translation. 
# If the user enters a grade lower than zero or higher than 10, just give an error message. Y
# ou do not need to handle the user entering grades that do not end in .0 or .5, though you may do that 
# if you like – in that case, if the user enters such an illegal grade, give an appropriate error message.
