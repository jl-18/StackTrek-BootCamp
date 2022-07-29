import os
os.system('cls||clear')

# Code starts here

M = int(input())
N = int(input())
P = int(input())
S = 2


for num in range(M, N + 1):
  for i in range(S, P + 1):
    if P == i:
      print(f"{num ** i}", end = "")
    elif P > i:
      print(f"{num ** i}", end = ", ")
  print()
      
#----Table of Powers----
#Write a program that displays the table of powers based on the following input:

#M - starting base
#N - ending base
#P - ending power (starting power is 2)
#So if the input are: M = 7 N = 14 P = 5
#The program will show the results of:

#7^2, 7^3, 7^4, 7^5
#8^2, 8^3, 8^4, 8^5
#9^2, 9^3, 9^4, 9^5
# 10^2, 10^3, 10^4, 10^5
# 11^2, 11^3, 11^4, 11^5
# 12^2, 12^3, 12^4, 12^5
# 13^2, 13^3, 13^4, 13^5
# 14^2, 14^3, 14^4, 14^5
# Numbers are separated by commas.

