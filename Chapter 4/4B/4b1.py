import os
os.system('cls||clear')

# Code starts here

first = int(input())
second = int(input())
third = int(input())

total = first + second + third
mins = total // 60
second = total % 60

if second < 10:
  print(f"{mins}:0{second}")
else:
  print(f"{mins}:{second}")

#----100 meter dash athletes -----
#Three 100m dash athletes finished in particular number of seconds (between 1 and 50). 
# Write a program that introduces the time of the contestants and calculates their total 
# time in "minutes:seconds" format.
#Note : Seconds needs to be in zero format (02, 03, etc...)
