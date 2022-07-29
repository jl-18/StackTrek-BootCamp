import os
os.system('cls||clear')

# Code starts here

string = input()
count = 0
if ("a" in string) or ("A" in string):
  count += 1
if ("e" in string) or ("E" in string):
  count += 1
if ("i" in string) or ("I" in string):
  count += 1
if ("o" in string) or ("O" in string):
  count += 1
if ("u" in string) or ("U" in string):
  count += 1

if count == 1:
  print("There is only one different vowel in the string.")
elif count > 1:
  print(f"There are {count} different vowels in the string.")
else:
  print("Invalid!Try again!")

  #----Vowel detector-----
  #Ask the user to supply a string. Print how many different vowels there are in the string. 
  # The capital version of a lower case vowel is considered to be the same vowel. 
  # y is not considered a vowel. Try to print nice output (e.g., printing “There are 1 different vowels in 
  # the string” is ugly).

  
