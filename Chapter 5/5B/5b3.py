import os
os.system('cls||clear')

# Code starts here

n = int(input())
factorial = 1

while n > 0:
  factorial *= n
  n -= 1
print(factorial)

#----Factorial---
#The factorial of a positive integer is that integer, multiplied by all positive integers that are lower 
# (excluding zero). You write the factorial as the number with an exclamation mark after it. 
# E.g., the factorial of 5 is 5! = 5 ∗ 4 ∗ 3 ∗ 2 ∗ 1 = 120. Write some code that calculates the factorial 
# of a number. Do not test your program with numbers that are too high, as factorials grow exponentially 
# (testing it up to 10! is more than enough). Hint: to do this with a while loop, you need two variables: 
# one variable which at the end of the loop must contain the answer, and one variable that contains the 
# current factor. In the loop, you multiply the answer with the current factor, before subtracting 1 from 
# the factor. Choose the right initialization of these variables before the loop.
#Note : Do not use any python library
