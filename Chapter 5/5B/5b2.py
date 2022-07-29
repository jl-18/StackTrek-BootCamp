import os
os.system('cls||clear')

# Code starts here

n = int(input())
count = 1
ave = 0

if n == 0:
  print("No entries")
else:
  ave = n
  while n != 0:
    n = int(input())
    if n == 0:
      continue
    ave += n
    count += 1
    
ave /= count
print(int(ave))
  
#-------Average-------
#In this exercise you will create a program that computes the average of a collection of values 
#entered by the user. The user will enter 0 to indicate that no further values will be provided. 
# Your program should display an error message No entries if the first value entered by the user is 0.
